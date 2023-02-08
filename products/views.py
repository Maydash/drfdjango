from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.forms import model_to_dict
# from django.shortcuts import render
from .models import Product, Comment, Group
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class ProductAPIListpagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 1000


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)   
    pagination_class = ProductAPIListpagination


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    permission_classes = (IsOwnerOrReadOnly,) 


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)   

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return Product.objects.all()[:3]

#     @action(methods=['get'], detail=True)
#     def group(self, request, pk=None):
#         group = Group.objects.get(pk=pk)
#         return Response({'group': group.title})

# class ProductAPIList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductAPIUpdate(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductAPIView(APIView):
#     def get(self, request):
#         w = Product.objects.all()
#         return Response({'product': ProductSerializer(w, many=True).data})

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Product.objects.get(pk=pk) 
#         except:
#             return Response({"error": "Method PUT not allowed"})

#         serializer = ProductSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})

#         try:
#             instance = Product.objects.get(pk=pk) 
#         except:
#             return Response({"error": "Method DELETE not allowed"})

#         instance.delete()
#         print(instance)
#         return Response({"post": f'Object {instance} is deleted'})