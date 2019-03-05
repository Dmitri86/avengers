from django.shortcuts import render


def show(request):
    return render(request, 'thor/thor.html')


# Create your views here.
