from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:animal_id>/weightings/', views.animal_weightings, name='animal_weightings'),
    path('my-animals/', views.my_animals, name='my_animals'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path('add-weighting/<int:animal_id>/', views.add_weighting, name='add_weighting'),
]
