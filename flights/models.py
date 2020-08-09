from django.db import models
#below here new class can be understood as new table
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
#keep in mind that each model is a python class and we need
#one model for one main table that we care about.
#below the parameters models.Model is representing the inheritance that class
#flight is inheriting from.
class Flight(models.Model):
#after adding any foreign airport connected to this flight we don't manu
#add a airpot but the foreign key to the origin variable
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
#above models.cascade means that if I ever delete an airport from the 
#airpot table, it is also going to delete any of those corresponding
#flights.
#there is also models.protect saying don't even let me delete the airport.
#also, the realated name creates the relationship between flight and airport
#in reverse order like for an airport how do I get all the flights with 
# that origin. using this related name to the foreign key Django would
#automatically create the relationship for us.
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
#here related name means if I have an airport, I might want to access all 
#the arrival of the flights corresponding to flights arriving at a destinat.
    duration = models.IntegerField()
#here presense of self means it automatically runs when the class is called
    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"
#below we will be creating a Flight test func to do the unittest
    def is_valid_flight(self):
        return self.origin != self.destination or self.duration >=0

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights= models.ManyToManyField(Flight,blank = True,related_name="passengers")
#a single passenger might have multiple flights.blank representing that 
# the passenger might also have no flights and related name saying if
#  have passenger can access all flights and if flights can use this to
#  access all the passengers on the flight.
    def __str__(self):
        return f"{self.first} {self.last}"