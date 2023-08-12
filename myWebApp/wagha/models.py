import uuid
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="product label")
    image = CloudinaryField('product_image', default="")
    description = models.CharField(max_length=1000, default="description")
    price = models.IntegerField(default=0)


class Rating(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    value = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.value}'
class Tag(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="tag")

    def __str__(self):
        return f'{self.label}'
class Size(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="size")

    def __str__(self):
        return f'{self.label}'
class Color(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="color")
    def __str__(self):
        return f'{self.label}'
class Material(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="material")
    def __str__(self):
        return f'{self.label}'





