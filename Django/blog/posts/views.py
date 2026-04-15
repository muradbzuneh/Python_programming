from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>This is the about page.</p>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>This is the contact page.</p>")