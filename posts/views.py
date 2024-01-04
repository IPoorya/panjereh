from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApartmentSellSerializer, ApartmentRentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from.models import ApartmentRent, ApartmentSell
from permissions import IsOwnerOrReadOnly



class CreatePostApiView(APIView):
    """
    create post

    type parametre values: sell, rent

    example: /post/2/create/

    **note**

    response schema could be different depend on the post type(sell or rent)

    differneces:
    in sell there is "total_price" field, but in rent there are "high_deposite", "low_rent", "low_deposite" and "high_rent" fields

    so don't worry about response schema, we just put sell schema as default response schema for swagger
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ApartmentSellSerializer

    def post(self, request, type):
        if type == 'rent':
            srz_data = ApartmentRentSerializer(data=request.data)
        elif type == 'sell':
            srz_data = ApartmentSellSerializer(data=request.data)

        if srz_data.is_valid():
            srz_data.validated_data['owner'] = request.user
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetPostApiView(APIView):
    """
    get posts using timestamp(temp)

    **note**

    response schema could be different depend on the post type(sell or rent)

    differneces:
    in sell there is "total_price" field, but in rent there are "high_deposite", "low_rent", "low_deposite" and "high_rent" fields

    so don't worry about response schema, we just put sell schema as default response schema for swagger
    """


    permission_classes = [AllowAny]
    serializer_class = ApartmentSellSerializer

    def get(self, request, timestamp):
        timestamp = str(timestamp)
        if timestamp[0] == '1':
            post = ApartmentSell.objects.filter(timestamp=timestamp).first()
            if post:
                post = ApartmentSellSerializer(instance=post)
                return Response(post.data, status=status.HTTP_200_OK)
            return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        elif timestamp[0] == '2':
            post = ApartmentRent.objects.filter(timestamp=timestamp).first()
            if post:
                post = ApartmentRentSerializer(instance=post)
                return Response(post.data, status=status.HTTP_200_OK)
            return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)
            

    


class EditPostApiView(APIView):
    """
    edit post using timestamp(temp)

    **note**

    response schema could be different depend on the post type(sell or rent)

    differneces:
    in sell there is "total_price" field, but in rent there are "high_deposite", "low_rent", "low_deposite" and "high_rent" fields

    so don't worry about response schema, we just put sell schema as default response schema for swagger
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ApartmentSellSerializer

    def put(self, request, timestamp):
        timestamp = str(timestamp)
        if timestamp[0] == '1':
            post = ApartmentSell.objects.filter(timestamp=timestamp)
        elif timestamp[0] == '2':
            post = ApartmentRent.objects.filter(timestamp=timestamp)

        if post:
            post = post[0]
            self.check_object_permissions(request, post)
            if timestamp[0] == '1':
                srz_data = ApartmentSellSerializer(data=request.data, instance=post, partial=True)
            elif timestamp[0] == '2':
                srz_data = ApartmentRentSerializer(data=request.data, instance=post, partial=True)
            
            if srz_data.is_valid():
                srz_data.save()
                return Response(srz_data.data, status=status.HTTP_200_OK)
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)


class DeletePostApiView(APIView):
    """
    delete post using timestamp(temp)
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, timestamp):
        timestamp = str(timestamp)
        if timestamp[0] == '1':
            post = ApartmentSell.objects.filter(timestamp=timestamp)
        elif timestamp[0] == '2':
            post = ApartmentRent.objects.filter(timestamp=timestamp)

        if post:
            post = post[0]
            self.check_object_permissions(request, post)
            post.delete()
            return Response({"message": "post deleted"}, status=status.HTTP_200_OK)
        return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)
        