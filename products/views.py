from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
# from django.shortcuts import render
from .models import Product, Comment, Group
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        w = Product.objects.all()
        return Response({'product': ProductSerializer(w, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})