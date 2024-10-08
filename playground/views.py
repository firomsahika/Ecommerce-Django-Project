from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q,F
from store.models import Product,OrderItem,Order,Customer

def say_hello(request):
    # Get the last five orders with their customer and items (including Product)
    
    queryset = OrderItem.objects.select_related('product').order_by('-order__placed_at')[:10]

    
    
   
    return render(request, 'core/index.html',{
        'orderitems': queryset,
    })