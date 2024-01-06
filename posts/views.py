from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApartmentSellSerializer, ApartmentRentSerializer, PostFiltersSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from.models import ApartmentRent, ApartmentSell
from permissions import IsOwnerOrReadOnly
from .cities import province, city



class CreatePostApiView(APIView):
    """
    create post

    type parametre values: sell, rent

    example: /post/sell/create/

    **note**

    response schema could be different depend on the post type(sell or rent)

    differneces:
    in sell there is "total_price" field, but in rent there are "high_deposite", "low_rent", "low_deposite" and "high_rent" fields

    so don't worry about response schema, we just put rent schema as default response schema in swagger
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ApartmentRentSerializer

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
    get post using token

    **note**

    response schema could be different depend on the post type(sell or rent)

    differneces:
    in sell there is "total_price" field, but in rent there are "high_deposite", "low_rent", "low_deposite" and "high_rent" fields

    so don't worry about response schema, we just put sell schema as default response schema in swagger
    """
    permission_classes = [AllowAny]
    serializer_class = ApartmentSellSerializer

    def get(self, request, token):
        if token[0] == 'S':
            post = ApartmentSell.objects.filter(token=token).first()
            if post:
                post = ApartmentSellSerializer(instance=post)
                return Response(post.data, status=status.HTTP_200_OK)
            return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        elif token[0] == 'R':
            post = ApartmentRent.objects.filter(token=token).first()
            if post:
                post = ApartmentRentSerializer(instance=post)
                return Response(post.data, status=status.HTTP_200_OK)
            return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)
            

    


class EditPostApiView(APIView):
    """
    edit post using token

    **note**

    response schema could be different depend on the post type(sell or rent)

    differneces:
    in sell there is "total_price" field, but in rent there are "high_deposite", "low_rent", "low_deposite" and "high_rent" fields

    so don't worry about response schema, we just put sell schema as default response schema in swagger
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ApartmentSellSerializer

    def put(self, request, token):
        if token[0] == 'S':
            post = ApartmentSell.objects.filter(token=token).first()
        elif token[0] == 'R':
            post = ApartmentRent.objects.filter(token=token).first()

        if post:
            self.check_object_permissions(request, post)
            if token[0] == 'S':
                srz_data = ApartmentSellSerializer(data=request.data, instance=post, partial=True)
            elif token[0] == 'R':
                srz_data = ApartmentRentSerializer(data=request.data, instance=post, partial=True)
            
            if srz_data.is_valid():
                srz_data.save()
                return Response(srz_data.data, status=status.HTTP_200_OK)
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)


class DeletePostApiView(APIView):
    """
    delete post using token
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, token):
        if token[0] == 'S':
            post = ApartmentSell.objects.filter(token=token).first()
        elif token[0] == 'R':
            post = ApartmentRent.objects.filter(token=token).first()

        if post:
            self.check_object_permissions(request, post)
            post.delete()
            return Response({"message": "post deleted"}, status=status.HTTP_200_OK)
        return Response({"Error": "not found!"}, status=status.HTTP_404_NOT_FOUND)
    

class GetCitiesApiView(APIView):
    """
    get provinces and cities list
    """
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"province": province, "city": city}, status=status.HTTP_200_OK)


class SellListApiView(APIView):
    """
    filters are optional.

    If a timestamp is not provided, the last 20 posts will be returned. However, if a timestamp is provided, then the 20 posts before that timestamp will be returned.
    """

    permission_classes = [AllowAny]
    serializer_class = PostFiltersSerializer


    def post(self, request):
        sells = ApartmentSell.objects.all().order_by("-id")
        if not sells:
            return Response({"error": "no data"}, status=status.HTTP_404_NOT_FOUND)
        if request.data:
            filters = PostFiltersSerializer(data=request.data)
            
            if filters.is_valid():      
                # applying filters
                if filters.validated_data.get('timestamp', None):
                    timestamp = filters.validated_data.get('timestamp', None)
                    sells = sells.filter(timestamp__lt=filters.validated_data.get('timestamp', None))
                if filters.validated_data.get('province', None):
                    sells = sells.filter(province__in=filters.validated_data.get('province', None))
                if filters.validated_data.get('city', None):
                    sells = sells.filter(city__in=filters.validated_data.get('city', None))
                if filters.validated_data.get('meterage', None):
                    sells = sells.filter(meterage=filters.validated_data.get('meterage', None))
                if filters.validated_data.get('build', None):
                    sells = sells.filter(build=filters.validated_data.get('build', None))
                if filters.validated_data.get('elevator', None):
                    sells = sells.filter(elevator=filters.validated_data.get('elevator', None))
                if filters.validated_data.get('parking', None):
                    sells = sells.filter(parking=filters.validated_data.get('parking', None))
                if filters.validated_data.get('storage', None):
                    sells = sells.filter(storage=filters.validated_data.get('storage', None))
            else:
                return Response(filters.errors, status=status.HTTP_400_BAD_REQUEST)

        
        # getting and sending posts
        if sells:
            sells = sells[:20]
            timestamp = sells[-1].timestamp
            sells = ApartmentRentSerializer(sells, many=True)
            return Response({
                "timestamp": timestamp,
                "posts": sells.data
                }, status=status.HTTP_200_OK)
        return Response({
                "timestamp": timestamp,
                "error": "no data",
                }, status=status.HTTP_200_OK)

    


class RentListApiView(APIView):
    """
    filters are optional.

    If a timestamp is not provided, the last 20 posts will be returned. However, if a timestamp is provided, then the 20 posts before that timestamp will be returned.
    """

    permission_classes = [AllowAny]
    serializer_class = PostFiltersSerializer


    def post(self, request):
        rents = ApartmentRent.objects.all().order_by("-id")
        if not rents:
            return Response({"error": "no data"}, status=status.HTTP_404_NOT_FOUND)
        if request.data:
            filters = PostFiltersSerializer(data=request.data)
            
            if filters.is_valid():      
                # applying filters
                if filters.validated_data.get('timestamp', None):
                    timestamp = filters.validated_data.get('timestamp', None)
                    rents = rents.filter(timestamp__lt=filters.validated_data.get('timestamp', None))
                if filters.validated_data.get('province', None):
                    rents = rents.filter(province__in=filters.validated_data.get('province', None))
                if filters.validated_data.get('city', None):
                    rents = rents.filter(city__in=filters.validated_data.get('city', None))
                if filters.validated_data.get('meterage', None):
                    rents = rents.filter(meterage=filters.validated_data.get('meterage', None))
                if filters.validated_data.get('build', None):
                    rents = rents.filter(build=filters.validated_data.get('build', None))
                if filters.validated_data.get('elevator', None):
                    rents = rents.filter(elevator=filters.validated_data.get('elevator', None))
                if filters.validated_data.get('parking', None):
                    rents = rents.filter(parking=filters.validated_data.get('parking', None))
                if filters.validated_data.get('storage', None):
                    rents = rents.filter(storage=filters.validated_data.get('storage', None))
            else:
                return Response(filters.errors, status=status.HTTP_400_BAD_REQUEST)

        
        # getting and sending posts
        if rents:
            rents = rents[:20]
            timestamp = rents[-1].timestamp
            rents = ApartmentRentSerializer(rents, many=True)
            return Response({
                "timestamp": timestamp,
                "posts": rents.data
                }, status=status.HTTP_200_OK)
        return Response({
                "timestamp": timestamp,
                "error": "no data",
                }, status=status.HTTP_200_OK)
        
        
        