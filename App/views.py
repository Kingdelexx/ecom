from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    items = Book.objects.filter(available=True)
    context={'items':items}
    return render(request, 'index.html',context)