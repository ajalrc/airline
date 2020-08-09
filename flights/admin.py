from django.contrib import admin
#we are here trying to import flight and airport model to our admin app to
#be able to manipulate it 
from .models import Flight,Airport,Passenger
# Register your models here.
admin.site.register(Airport)#this registration is giving us manipul. power
class FlightAdmin(admin.ModelAdmin):#here I am configuring admin.py to show
#me all these display for flights
    list_display=("id","origin","destination","duration")
admin.site.register(Flight,FlightAdmin)#here ,flightadmin means that I 
#will be able to see the settings described above

class PassengerAdmin(admin.ModelAdmin):#this class is a little bit more
#better way of manipulating the flights for the passenger where we get to
# know in which flights the passenger are already on and which flights can
#still be added for them. Here filter_horizontal is not a variable but a
#preserved attribute.
    filter_horizontal=("flights",)
admin.site.register(Passenger,PassengerAdmin)