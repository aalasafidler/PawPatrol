from django.shortcuts import render, redirect
from .models import Record, Pet
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def pets(request):
    pets = Pet.objects.filter(author=request.user)
    numberOfPets = len(pets)
    return render(request, 'records/pets.html', {'pets': pets}, numberOfPets)

@login_required(login_url="/accounts/login/")
def records(request):

    thisauthor = request.user
    thisfeed = Record.objects.all()
    """
    amountDispensed = Record.objects.get(feedID=6).amountDispensed
    amountConsumed = amountLeftOver - amountDispensed
    totaldispensed = Record.objects.aggregate(Sum('amountDispensed'))"""

    records = Record.objects.filter(author=request.user)
    return render(request, 'records/records.html', {'records': records, 'this-author': thisauthor, 'thisfeed': thisfeed},)

@login_required(login_url="/accounts/login/")
def add_pet(request):
    thisauthor = request.user
    if request.method == 'POST':
        form = forms.AddPet(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('yourPet')
    else:
        form = forms.AddPet()
    return render(request, 'records/pet_create.html', {'form': form, 'this-author': thisauthor},)


@login_required(login_url="/accounts/login/")
def record_create(request):
    pets = Pet.objects.filter(author=request.user)

    if request.method == 'POST':
        form = forms.CreateRecord(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('records')
    else:
        form = forms.CreateRecord()
    return render(request, 'records/record_create.html', {'form': form})

@login_required(login_url="/accounts/login/")
def your_pet(request):
    pets = Pet.objects.filter(author=request.user)
    numberOfPets = len(pets)
    if numberOfPets == 0:
        x = 1
    else:
        x = numberOfPets + 1

    return render(request, 'records/your-pet.html', {'pets': pets, 'number': x},)

def stats(request):
    numberofpets = Pet.objects.filter(author=request.user)
    j = 0
    pets = Pet.objects.filter(author=request.user)
    petNames = Pet.objects.filter(author=request.user)[j].petName
    thisauthor = request.user
    feeds = Record.objects.filter(author=request.user)
    numberoffeeds = len(feeds) + 3

    numberOfPets = len(pets)
    myRecords = Record.objects.filter(author=request.user)
    totalleftover = myRecords.aggregate(Sum('amountLeftOver'))['amountLeftOver__sum'] + 15
    totaldispensed = myRecords.aggregate(Sum('amountDispensed'))['amountDispensed__sum'] + 250

    totalConsumed = totaldispensed - totalleftover
    avgconsumed = totalConsumed/numberoffeeds
    avgleftover = totalleftover/numberoffeeds
    #ludo = myRecords.filter(selectPet="Ludo")
    #ludoID = ludo[0].feedID
    #ludoConsumed = ludo[0].amountLeftOver
    #karen = myRecords.filter(selectPet="Karen")

    #individualConsumed = Record.objects.filter(author=request.user)[j].petName
    #individualLeftOver =

    return render(request, 'records/stats.html', {'myRecords': myRecords, 'pets': pets, 'this-author': thisauthor, 'numberoffeeds': numberoffeeds, 'totaldispensed': totaldispensed, 'totalleftover':totalleftover, 'numberofpets': numberofpets, 'totalConsumed': totalConsumed, 'avgconsumed': avgconsumed, 'avgleftover': avgleftover},)

#'ludoConsumed': ludoConsumed, 'ludoID': ludoID, aren': karen, '
