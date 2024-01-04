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
        