from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
from .models import Group, Comment, Product


# class ProductModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # добавляет скрытое поле в форму создание со значением пользователя 
    class Meta:
        model = Product
        fields = "__all__" 


    # group_id = serializers.IntegerField()
    # title = serializers.CharField(max_length=100)
    # description = serializers.CharField()
    # quantity = serializers.IntegerField()
    # code = serializers.IntegerField()
    # price = serializers.FloatField()
    # time_create = serializers.DateField(read_only=True)
    # time_update = serializers.DateField(read_only=True)

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.quantity = validated_data.get("quantity", instance.title)
    #     instance.code = validated_data.get("code", instance.code)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.save()
    #     return instance




# def encode():
#     model = ProductModel('title', 'description')
#     model_r = ProductSerializer(model)
#     print(model_r.data, type(model_r), sep="\n")
#     json = JSONRenderer().render(model_r.data)
#     print(json)