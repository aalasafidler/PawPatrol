from django.shortcuts import render, redirect
from .models import Record, Pet
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def records(request):
    records = Record.objects.all()#.order_by(dateTime)
    # The dictionary outputs the variable records (above)
    # when rendered. Display it in the records.html template
    # via "template tags" = {% python code %} and {{data}}
    return render(request, 'records/records.html', {'records': records})

@login_required(login_url="/accounts/login/")
def record_create(request):
    if request.method == 'POST':
        form = forms.CreateRecord(request.POST, request.FILES)
        if form.is_valid():
            # save this record to database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('records')
    else:
        form = forms.CreateRecord()
    return render(request, 'records/record_create.html', {'form': form})
    #return redirect('/')

@login_required(login_url="/accounts/login/")
def pets(request):
    pets = Pet.objects.all()
    numberOfPets = len(pets)
    return render(request, 'records/pets.html', {'pets': pets}, numberOfPets)

@login_required(login_url="/accounts/login/")
def add_pet(request):
    if request.method == 'POST':
        form = forms.AddPet(request.POST, request.FILES)
        if form.is_valid():
            # save this record to database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('pets')
    else:
        form = forms.AddPet()
    return render(request, 'records/pet_create.html', {'form': form})
    #return redirect('/')
