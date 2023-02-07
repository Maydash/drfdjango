from django.db import models


class Group(models.Model):
    '''Группы для товаров'''
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.group} : {self.title}'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    time_create = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.author