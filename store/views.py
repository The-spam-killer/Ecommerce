from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#Test Only

def index(request):
    return HttpResponse("Hello There!")


def store(request):
    context = {}
    return render(request,'store/store.html')

def cart(request):
    context = {}
    return render(request,'store/cart.html')

def checkout(request):
    context = {}
    return render(request,'store/checkout.html')
