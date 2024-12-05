from django.contrib import admin
from .models import AnimalType, Breed, Animal, Weighting

@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'animaltype')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'inventory_number', 'gender', 'breed', 'arrival_date', 'arrival_age_months')
    search_fields = ('name', 'inventory_number')

@admin.register(Weighting)
class WeightingAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'weight_kg')
    list_filter = ('animal', 'date')
    search_fields = ('animal__name',)
