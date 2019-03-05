from django.shortcuts import render


def show(request):
    return render(request, 'black_widow/black_widow.html')

# Create your views here.
