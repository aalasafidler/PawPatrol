from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def your_pet(request):
    # return HttpResponse('about')
    return render(request, 'your-pet.html')

