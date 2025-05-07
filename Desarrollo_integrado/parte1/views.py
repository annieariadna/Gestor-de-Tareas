from django.shortcuts import render, redirect

# Create your views here.
def layout(request):
    return render(request,'layouts.html')

def index (request):
    return render(request,'index.html')