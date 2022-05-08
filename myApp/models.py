from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

Size_breed_choice = [
    ('Tiny', 'Tiny'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large')
]


# Breed Model


class Breed (models.Model):
    breed_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10, choices=Size_breed_choice)
    friendliness = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    trainability = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    sheddingamount = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    exerciseneeds = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )


# Dog Model
class Dog(models.Model):
    dog_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    foreign_breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)

