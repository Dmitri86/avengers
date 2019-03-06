from django.shortcuts import render


def show(request):
    return render(request, 'hulk/hulk.html')

# Create your views here.
