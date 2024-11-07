from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')


def base(request):
    return render(request, 'base.html')