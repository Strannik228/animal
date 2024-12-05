from datetime import date
from django.db import models
from django.conf import settings  # Импортируем настройки для использования AUTH_USER_MODEL

class AnimalType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=50)
    animaltype = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Animal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    inventory_number = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    name = models.CharField(max_length=50, null=True, blank=True)
    arrival_date = models.DateField()
    arrival_age_months = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='offspring')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='animals')  # Используем AUTH_USER_MODEL

    def __str__(self):
        return self.name

    def age(self):
        today = date.today()
        arrival_age_years = self.arrival_age_months // 12
        arrival_age_remaining_months = self.arrival_age_months % 12
        age_years = today.year - self.arrival_date.year + arrival_age_years
        age_months = today.month - self.arrival_date.month + arrival_age_remaining_months
        if age_months >= 12:
            age_years += 1
            age_months -= 12
        if age_months < 0:
            age_years -= 1
            age_months += 12

        if age_years == 1:
            year_str = "1 г"
        elif 2 <= age_years <= 4:
            year_str = f"{age_years} г"
        else:
            year_str = f"{age_years} л"

        month_str = f"{age_months} м"

        return f"{year_str} {month_str}"

class Weighting(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('animal', 'date')

    def __str__(self):
        return f'{self.animal.name} - {self.date}'
