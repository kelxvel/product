from django.shortcuts import render
from django.utils import timezone
from django.core.exceptions import PermissionDenied
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

def new_products(request):
    if request.user.is_authenticated():
        time = timezone.now() - timezone.timedelta(hours = 24)
        products = Product.objects.filter(created_at__gt = time)
        return render(request, 'new_products.html', {'products': products})
    else:
        raise PermissionDenied 
