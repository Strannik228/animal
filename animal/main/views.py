from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Animal, AnimalType, Breed, Weighting
from .forms import AnimalForm, WeightingForm

def animal_list(request):
    query = request.GET.get('q')
    selected_type = request.GET.get('type')
    selected_breed = request.GET.get('breed')
    arrival_date_from = request.GET.get('arrival_date_from')
    arrival_date_to = request.GET.get('arrival_date_to')

    animals = Animal.objects.all()

    if query:
        animals = animals.filter(Q(inventory_number__icontains=query) | Q(name__icontains=query))
    if selected_type:
        animals = animals.filter(breed__animaltype__id=selected_type)
    if selected_breed:
        animals = animals.filter(breed__id=selected_breed)
    if arrival_date_from:
        animals = animals.filter(arrival_date__gte=arrival_date_from)
    if arrival_date_to:
        animals = animals.filter(arrival_date__lte=arrival_date_to)

    animal_types = AnimalType.objects.all()
    breeds = Breed.objects.all()

    context = {
        'animals': animals,
        'query': query,
        'selected_type': selected_type,
        'selected_breed': selected_breed,
        'arrival_date_from': arrival_date_from,
        'arrival_date_to': arrival_date_to,
        'animal_types': animal_types,
        'breeds': breeds,
    }

    return render(request, 'main/animal_list.html', context)

def animal_weightings(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    weightings = animal.weighting_set.all().order_by('-date')
    return render(request, 'main/animal_weightings.html', {'animal': animal, 'weightings': weightings})

@login_required
def my_animals(request):
    animals = Animal.objects.filter(owner=request.user)
    return render(request, 'main/my_animals.html', {'animals': animals})

@login_required
def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.owner = request.user
            animal.save()
            return redirect('main:my_animals')
    else:
        form = AnimalForm()
    return render(request, 'main/add_animal.html', {'form': form})

@login_required
def add_weighting(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = WeightingForm(request.POST)
        if form.is_valid():
            weighting = form.save(commit=False)
            weighting.animal = animal
            weighting.save()
            return redirect('main:my_animals')
    else:
        form = WeightingForm()
    return render(request, 'main/add_weighting.html', {'form': form, 'animal': animal})
