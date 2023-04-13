from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductListView(ListView):
    model = Product
    #'product_list.html',{'product_list':product.objects.all()}

class ProductDetailView(DetailView):
    model = Product
    #'Product_detail.html',{'Product' : Product.object.get(pk = pk)}