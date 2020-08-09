from django.test import TestCase,Client
from django.db.models import Max
from .models import Airport,Flight,Passenger
class FlightTestCase(TestCase):
    def setUp(self):
#below are some of the dummy airports and dummy flights that were created
        a1=Airport.objects.create(code="AAA",city="City A")
        a2=Airport.objects.create(code="BBB",city="City B")

        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)
#below, I am making sure that the departure count is working as needed.
    def test_departures_count(self):
        a=Airport.objects.get(code="AAA")#get the flight whose code is AAA
        self.assertEqual(a.departures.count(),3)
    
    def test_arrivals_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),1)
    
    def test_valid_flight(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=100)
        self.assertTrue(f.is_valid_flight())#this is to verify the valid 
    #flight condition.

    def test_invalid_flight_destination(self):
        a1=Airport.objects.get(code="AAA")#we don't even need to pass the 
#third parameter if the first one is already false.
        f=Flight.objects.get(origin=a1,destination=a1)
        self.assertFalse(f.is_valid_flight())#this is to verify that this 
# condition should not happen.     
    def test_invalid_flight_duration(self):
            a1=Airport.objects.get(code="AAA")
            a2=Airport.objects.get(code="BBB")
            f=Flight.objects.get(origin=a1,destination=a2,duration=-100)
            self.assertFalse(f.is_valid_flight())#this is to verify that this 
 #condition should not happen. 
    def test_index(self):
        c=Client()#this is the client that is going to be interacting 
#response and request style
        response=c.get("/flights/")#this is the route that gets me the 
#index page for all the flights which  I am saving in a variable to have
#multiple assert tests
        self.assertEqual(response.status_code,200)#this means the response
#that we are getting is good to go.
        self.assertEqual(response.context["flights"].count(),3)#here I am
#access the body of the webpage and since we have created three flights
#here the flight count better be 3.
    def test_valid_flight_page(self):
        a1=Airport.objects.get(code="AAA")
        f=Flight.objects.get(origin=a1,destination=a1)#we will get this 
#flight because it exists in the database.
        c=Client()
        response=c.get(f"/flights/{f.id}")#here I am able to get the id
#cause it exists and is valid.
        self.assertEqual(response.status_code,200)#and thus this should
#have a status code of 200.

    def test_flight_page_passengers(self):
        f=Flight.objects.get(pk=1)#added a sample passenger
        p=Passenger.objects.create(first="Alice",last="Adams")
        f.passengers.add(p)
        c=Client()
        response= c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["passengers"].count(),1)#after
#adding the passenger, I am making sure that the passengers count is cor
#rect.
    def test_flight_page_non_passengers(self):#this is just the opposite
#idea of above equation.
        f=Flight.objects.get(pk=1)
        p=Passenger.objects.create(first="Alice",last="Adams")
        c=Client()
        response=c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["non_passengers"].count(),1)