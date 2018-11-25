from django import forms
from . import models

class CreateRecord(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = ['feedID', 'amountLeftOver', 'amountDispensed', 'additionalInfo']

class AddPet(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ['petName', 'petImage']
