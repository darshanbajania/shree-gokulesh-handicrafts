from django.shortcuts import render
from .models import Product, Advertisement
# Create your views here.
from django.http import HttpResponse


def home(request):
    product_data = Product.objects.all()
    homeAdvertisementImage = Advertisement.objects.filter(label='HomePage').first()
    print("🚀 ~ file: views.py:10 ~ homeAdvertisementImage:", homeAdvertisementImage.image.url)

    context ={
        'product_data': product_data,
        'banner_url':homeAdvertisementImage.image.url
    }

    return render(request, 'wagha/base.html', context=context)