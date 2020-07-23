from django.db import models

# Create your models here.


class PlaceInfo(models.Model):
    placeName = models.CharField(max_length=200)
    placeCountry = models.CharField(max_length=200)
    arrivalTime = models.CharField(max_length=200)
    departureTime = models.CharField(max_length=200)
    experience = models.TextField(max_length=1000)
    def __str__(self):
        return self.placeCountry

class ContactInfo(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    def __str__(self):
        return self.firstName