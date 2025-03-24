from django.db import models

# Create your models here.
class Owner(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    number_of_pets = models.IntegerField(default=1)

class Cat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    breed = models.CharField()
    age = models.PositiveIntegerField()
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(default="Unknown")
    name = models.CharField(max_length=200)

class Dog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    age = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    vaccinated = models.BooleanField(default=False)
    breed = models.CharField()
    description = models.TextField(default="Unknown")

class Bird(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(default="Unknown")
    species = models.CharField()

class Exotic_Animal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    region_of_origin = models.CharField()
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    type_of_animal = models.CharField()
    vaccinated = models.BooleanField(default=False)