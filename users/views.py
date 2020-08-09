from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
#here I am saying that every user has a user attribute associated with and
#an authentication attribute that tells us if the user is signed in ornot
#if not the user then redirect to log in view
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")
def login_view(request):
    if request.method=="POST":
    #keep in mind that the method makes a difference, if the method is get
    #get then it just gives me the form, but for the post method, we submit
    #the data from the form as well
        username=request.POST["username"]#grabs the username named data
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)#here
#for authentication, I take the request, username and the password and 
#returns me who the user actually is.and if the information is wrong then
#provide a message
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{
                "message":"Invalid credentials."
            })
#to authenticate the username and password,  I import from django.auth
#authenticate, login and logout.
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
  #below means where should I take the user after he/she has been logout
    return render(request,"users/login.html",{
        "message":"Logged out"
    })