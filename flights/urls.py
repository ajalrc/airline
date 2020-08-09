from . import views
from django.urls import path
urlpatterns = [
#here before creating the path lets focus on creating the models that will 
# be our python class representing our data that I want django to store 
# inside a database when the model creation happens django is able to 
# figure out what syntax need to be used to a create the table and next
#  manipulate the table.
    path("",views.index,name="index"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book")#here /book indicates that I am able to
#book this id's flight
]