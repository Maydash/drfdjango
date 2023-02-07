from django.contrib import admin
from .models import Product, Group, Comment


admin.site.register(Group)
admin.site.register(Product)
admin.site.register(Comment)