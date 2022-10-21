from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import place

# Create your views here.
def home(request):
    obj=place.objects.all()
    return render(request,'index.html',{'res':obj})

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']

        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
                user.save()
                

        else:
            messages.info(request, "passwords are not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'reg.html')