from rest_framework.views import APIView
import json, os, pickle
import pandas as pd
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.permissions import AllowAny
from .serializers import PredictRentSerializer



class PricePerMeter(APIView):
    """
    price per meter

    send get request to fetch price per meter in each neighborhood (tehran)
    """

    permission_classes = [AllowAny]

    def get(self, request):
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the CSV file
        csv_path = os.path.join(current_dir, 'data', 'appartment_rent.csv')

        # Load your csv file into a pandas DataFrame
        df = pd.read_csv(csv_path)

        # Calculate the average rent price for each neighborhood
        average_rent = df.groupby('neighbourhood')['rent'].mean()

        # Convert the DataFrame to a JSON string
        average_rent_json = average_rent.to_json()

        # Convert the JSON string to a Python dictionary
        average_rent_dict = json.loads(average_rent_json)

        return Response(average_rent_dict, status=status.HTTP_200_OK)
    


class PredictRentPrice(APIView):
    """
    predict rent price

    send post request to predict rent price in a neighborhood (tehran)
    """

    permission_classes = [AllowAny]
    serializer_class = PredictRentSerializer

    def post(self, request):

        srz_data = PredictRentSerializer(data=request.data)
        if srz_data.is_valid():
            # Get the directory of the current file
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the path to the model file
            model1_path = os.path.join(current_dir, 'data', 'finalized_model_rent.sav')
            model2_path = os.path.join(current_dir, 'data', 'finalized_model_deposit.sav')

            # Load the models from disk
            loaded_model_rent = pickle.load(open(model1_path, 'rb'))
            loaded_model_deposit = pickle.load(open(model2_path, 'rb'))

            # Convert the dictionary to a DataFrame
            input_data = {
                'neighbourhood': [srz_data.validated_data.get('neighbourhood')],
                'meterage': [srz_data.validated_data.get('meterage')],
                'build': [srz_data.validated_data.get('build')],
                'room': [srz_data.validated_data.get('room')],
                'elevator': [srz_data.validated_data.get('elevator')],
                'parking': [srz_data.validated_data.get('parking')],
                'storage': [srz_data.validated_data.get('storage')]
            }
            input_df = pd.DataFrame(input_data)

            # Use the loaded models to make predictions
            predictions_rent = loaded_model_rent.predict(input_df)
            predictions_deposit = loaded_model_deposit.predict(input_df)

            return Response({'predictions_rent':predictions_rent, 'predictions_deposit':predictions_deposit}, status=status.HTTP_200_OK) 
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
