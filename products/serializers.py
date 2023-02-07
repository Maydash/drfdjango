from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Group, Comment, Product


# class ProductModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description


class ProductSerializer(serializers.Serializer):
    group = serializers.CharField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    code = serializers.IntegerField()
    price = serializers.FloatField()
    time_create = serializers.DateField(read_only=True)
    time_update = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


# def encode():
#     model = ProductModel('title', 'description')
#     model_r = ProductSerializer(model)
#     print(model_r.data, type(model_r), sep="\n")
#     json = JSONRenderer().render(model_r.data)
#     print(json)