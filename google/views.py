from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def action(request):
    return render(request, 'base.html')
# Create your views here.
