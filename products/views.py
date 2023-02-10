from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.forms import model_to_dict
# from django.shortcuts import render
from .models import Product, Comment, Group
from .serializers import ProductSerializer, GroupSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
# from .forms import Login_form


# class ProductAPIListpagination(PageNumberPagination):
#     page_size = 3
#     page_query_param = 'page_size'
#     max_page_size = 1000

class GroupAPIList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        # print(pk)
        if not pk:
            return Response({"error": "Method GET not allowed"})
            
        # instance = Product.objects.filter(group_id=pk).values()
        instance = Product.objects.filter(group=pk)
        group = Group.objects.filter(pk=pk)
        print(group)
        print(instance)
        
        return Response({'product': ProductSerializer(instance, many=True).data})
        # serializer = ProductSerializer(data=request.data, instance=instance, many=True)
        # serializer.is_valid(raise_exception=True)
        # return Response({"post": serializer.data})
        print(instance.data)
        # print(serializer.data)




class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)   
    # pagination_class = ProductAPIListpagination
    # parser_classes = [MultiPartParser]



class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    permission_classes = (IsAuthenticated,) 


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#     permission_classes = (IsAdminOrReadOnly,)   



# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     parser_classes = [MultiPartParser]

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