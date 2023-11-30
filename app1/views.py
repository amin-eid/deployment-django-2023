from django.shortcuts import render,redirect
from django.contrib import messages
import bcrypt

from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        
        return redirect("/")
    else:
        password= request.POST['password']
        hashed=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        usr=User.objects.create(first=request.POST['fname'],last=request.POST['lname'],email=request.POST['email'],password=hashed)
        request.session['guest']=usr.first
        request.session['id']=usr.id
        return redirect("/success")
    
def login(request):
    user=User.objects.filter(email=request.POST['email'])
    if user:
        logged=user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged.password.encode()):
            request.session['id']=logged.id
            request.session['guest']=logged.first
            return redirect("/success")
        else:
            messages.error(request,"Invalid credentials!")

            return redirect("/")
    else:

        messages.error(request,"Invalid credentials!")
        return redirect("/")

def main(request):
    if not 'id' in request.session:
        messages.error(request,"you have to login first!")
        return redirect("/")
    else:
        return render(request,"success.html")


def logout(request):
    request.session.flush()
    return redirect("/")