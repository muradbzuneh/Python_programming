from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about_us.html', context)

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>This is the contact page.</p>")
