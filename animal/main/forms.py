from django import forms
from .models import Animal, Weighting

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'inventory_number', 'gender', 'arrival_date', 'arrival_age_months', 'breed', 'parent']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
        }

class WeightingForm(forms.ModelForm):
    class Meta:
        model = Weighting
        fields = ['date', 'weight_kg']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
