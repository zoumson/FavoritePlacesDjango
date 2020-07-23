from django.shortcuts import render
from django.http import HttpResponse
from .models import PlaceInfo, ContactInfo
# Create your views here.


def index(request):
    allPlaces = PlaceInfo.objects.all()
    return render(request, "GoForHolidayApp/index.html", {'places': allPlaces})


def addPlace(request):
    return render(request, "GoForHolidayApp/addNewPlace.html")


def about(request):
    return render(request, "GoForHolidayApp/about.html")


def contact(request):
    return render(request, "GoForHolidayApp/contact.html")


def addPlaceSubmission(request):
    pNa = request.POST["place-name"]
    pCo = request.POST["place-country"]
    pAr = request.POST["time-arrival"]
    pDep = request.POST["time-arrival"]
    pExp = request.POST["place-experience"]
    placeInfo = PlaceInfo(placeName=pNa, placeCountry=pCo,
                          arrivalTime=pAr, departureTime=pDep, experience=pExp)
    placeInfo.save()
    allPlaces = PlaceInfo.objects.all()
    return render(request, "GoForHolidayApp/index.html", {'places': allPlaces})

def messageSubmission(request):
    fName = request.POST["contact-first-name"]
    lName = request.POST["contact-last-name"]
    email = request.POST["contact-email"]
    message = request.POST["contact-message"]
    contactInfo = ContactInfo(firstName =fName, lastName = lName,
                          email = email, message = message)
    contactInfo.save()
    return render(request, "GoForHolidayApp/contact.html")