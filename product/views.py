from django.shortcuts import render
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})    

def category_detail(request, category_slug):
    category = Category.objects.get(slug = category_slug)
    products = Product.objects.filter(category = category)
    return render(request, 'category_detail.html', {'products': products})

def product_detail(request, category_slug, product_slug):
    product = Product.objects.get(slug = product_slug)
    return render(request, 'product_detail.html', {'product': product})
