from django.contrib import admin

# Register your models here.
from .models import Product, Rating, Tag, Size, Color, Material, Image

admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Image)