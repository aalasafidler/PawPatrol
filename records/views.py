from django.shortcuts import render, redirect
from .models import Record, Pet
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def pets(request):
    #pets = Pet.objects.all()
    pets = Pet.objects.filter(author=request.user)
    numberOfPets = len(pets)
    return render(request, 'records/pets.html', {'pets': pets}, numberOfPets)

@login_required(login_url="/accounts/login/")
def records(request):
    records = Record.objects.filter(author=request.user)
    return render(request, 'records/records.html', {'records': records})

@login_required(login_url="/accounts/login/")
def add_pet(request):
    thisauthor = request.user
    if request.method == 'POST':
        form = forms.AddPet(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('yourPet')
    else:
        form = forms.AddPet()
    return render(request, 'records/pet_create.html', {'form': form, 'this-author': thisauthor},)


@login_required(login_url="/accounts/login/")
def record_create(request):
    if request.method == 'POST':
        form = forms.CreateRecord(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('records')
    else:
        form = forms.CreateRecord()
    return render(request, 'records/record_create.html', {'form': form})

@login_required(login_url="/accounts/login/")
def your_pet(request):
    pets = Pet.objects.filter(author=request.user)
    numberOfPets = len(pets)
    return render(request, 'records/your-pet.html', {'pets': pets, 'number': numberOfPets},)

def stats(request):
    thisauthor = request.user
    pets = Pet.objects.filter(author=request.user)
    feeds = Record.objects.all()
    totalconsumed = Record.objects.aggregate(Sum('amountDispensed'))
    avgconsumed = Record.objects.aggregate(Sum('amountLeftOver'))
    numberoffeeds = len(feeds)
    numberOfPets = len(pets)

    return render(request, 'records/stats.html', {'avgc': avgconsumed, 'pets': pets, 'totalconsumed': totalconsumed, 'numberofpets2': numberOfPets, 'numberoffeeds2': numberoffeeds, 'this-author': thisauthor},)
