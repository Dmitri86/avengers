from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request, "avengers/1.html")
