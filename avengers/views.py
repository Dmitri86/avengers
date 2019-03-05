from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    return HttpResponse("<img src=\"https://www.hdwallpapers.in/download/avengers_infinity_war_4k_8k-2560x1600.jpg\" alt=\"\" width=100% height=98.5%>")

# Create your views here.
