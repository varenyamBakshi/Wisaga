from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'wisaga/home.html')

def about(request):
    return render(request, 'wisaga/about.html')

def contact_us(request):
    return render(request, 'wisaga/contact_us.html')