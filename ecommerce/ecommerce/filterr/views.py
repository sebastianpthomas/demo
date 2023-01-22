from django.shortcuts import render
from  user_shop.models import Product




def sort_low_to_high(request):
    products= Product.objects.all().order_by('price')
    return render(request,'sort_page.html', {'products':products})