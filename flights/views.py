from django.shortcuts import render
from .models import Flight,Passenger
from django.urls import reverse
from django.http import HttpResponseRedirect

#here I will be rendering a template to display all the flights that I 
# will be adding here.see how the flights is calling all the object for
# Flight
def index(request):
    return render (request,"flights/index.html",{
        "flights":Flight.objects.all()
    })
def flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id) #here pk means the primary
 #key, we could also have used id=... to get the flight detail whose id is
 #equal to flight_id
    return render(request,"flights/flight.html",{
#the curly bracket means that when I render flight.htlm the below mentioned
#flight, respec. pass to flight and non passengers should be got.
        "flight":flight,
        "passengers":flight.passengers.all(),#this here is the way of 
#displaying the information of the passenger happening to be on any 
# given flight.We are able to do the related names where we are able
#to make this connection.
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
#this above non_pass. is excluding the passenger whose among the flights
#has the mentioned flight.
    })
def book(request,flight_id):
#the main focus here is when we are trying to submit the form or trying
#to manipulate the date then, it is always via the post request.
    if request.method=="POST":
#for the post method i.e to book a flight, I need the flight and the 
#passenger information here (need to create that form to call the post meth).
        flight=Flight.objects.get(pk=flight_id)#get me the flight with
#that flight id
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
#it means that the data about the  passenger would be received via a form 
# whose input field name is passe..
# for the passenger variable, that long structure is cause by default,the
#input is string so, we are converting the pk of the passenger to int 
#depending on the name of the "passenger"
        passenger.flights.add(flight)#here I will be adding that flight
#for that passenger in a new row, but I don't have to worry about the
#detail as django website would be working under the hood.
        return HttpResponseRedirect(reverse("flight",args=(flight.id,)))
 #here redirect is done in reverse to flight route which takes a particular
 #view like(flight,index,book) and gives me the url( like last time) 
 # and here flight url takes an argument which is the id number.