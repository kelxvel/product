from django.shortcuts import render
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})    

def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    products = Product.objects.filter(category = category)
    return render(request, 'category_detail.html', {'products': products})
