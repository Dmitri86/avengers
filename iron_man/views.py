from django.shortcuts import render


def show(request):
    return render(request, 'iron_man/iron_man.html')

# Create your views here.
