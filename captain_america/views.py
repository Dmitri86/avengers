from django.shortcuts import render


def show(request):
    return render(request, 'captain_america/Captain_America.html')

# Create your views here.
