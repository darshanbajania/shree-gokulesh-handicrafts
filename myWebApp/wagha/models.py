import uuid
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.




class Size(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="size")

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

class Tag(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="tag")

    def __str__(self):
        return f'{self.label}'
class Product(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="product label")
    
    description = models.CharField(max_length=1000, default="description")
    price = models.IntegerField(default=0)

    def get_default_size():
        """ get a UUID of a random size """
        random_size = Size.objects.order_by('?').first()  # Get a random size
        if random_size:
            return random_size
        else:
            default_size, _ = Size.objects.get_or_create(label="created")
            return default_size.id
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=get_default_size  )
    def get_default_material():

            default_size, _ = Material.objects.get_or_create(label="Cotton")
            return default_size.id
    material = models.ForeignKey(Material, on_delete=models.CASCADE, default=get_default_material )
    tags = models.ManyToManyField(Tag, related_name='products')


class Rating(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    value = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.value}'


class Color(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    label = models.CharField(max_length=200, default="color")
    def __str__(self):
        return f'{self.label}'


class Image(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('product_image', default="")


