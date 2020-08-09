from django.urls import path
from . import views

urlpatterns=[
#here the first route is for the currently login user,one route to log in 
#and the final route to log out.
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout")
]