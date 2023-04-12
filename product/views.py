from django.shortcuts import render
from django.views.generic import ListView

import product


class ProductListView(ListView):
    model = product
