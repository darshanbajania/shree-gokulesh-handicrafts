from django.shortcuts import render
from .models import Product, Advertisement
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from urllib.parse import urlencode
def Home(request):
    product_data = Product.objects.all()
    homeAdvertisementImage = Advertisement.objects.filter(label='HomePage').first()


    if request.method == "POST":
            # cart_contents.clear()
            # print(cart_contents)
            # print(request.session['cart_contents'])
        product_id = request.POST.get('product')
        view_all_type = request.POST.get('view-all-button')
        print("🚀 ~ file: views.py:17 ~ product_number:", product_id)
        if view_all_type != None:
            print(product_id)
            base_url = reverse('wagha:all_products')
            # creating a string of dictionary
            query_string = urlencode({'product': product_id})
            # passing the base_url and query from this page to url
            url = '{}?{}'.format(base_url, query_string)

            # print(proposal_number)
            return redirect(url)
        if product_id != None:
            # getting the url for displaying full proposal
            print(product_id)
            base_url = reverse('wagha:product_details')
            # creating a string of dictionary
            query_string = urlencode({'product': product_id})
            # passing the base_url and query from this page to url
            url = '{}?{}'.format(base_url, query_string)

            # print(proposal_number)
            return redirect(url)
    context ={
        'product_data': product_data,
        'banner_url':homeAdvertisementImage.image.url
    }
    return render(request, 'wagha/base.html', context=context)

def Product_details(request):
    current_product_id = request.GET.get('product')
        # print(current_product_id)
    selected_product = Product.objects.filter(id=current_product_id).first()
    print("🚀 ~ file: views.py:39 ~ selected_product:", selected_product)
    context ={
        'selected_product': selected_product,
    }

    return render(request, 'wagha/product_details.html', context=context)
def All_products(request):
    current_product_id = request.GET.get('product')
        # print(current_product_id)
    all_products = Product.objects.all()
    print("🚀 ~ file: views.py:39 ~ selected_product:", all_products)
    context ={
        'all_products': all_products,
    }

    return render(request, 'wagha/all_products.html', context=context)