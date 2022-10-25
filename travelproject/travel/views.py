from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import place


# Create your views here.
def home(request):
    obj=place.objects.all()
    return render(request,'index.html',{'obj':obj})




def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']

        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username already exist")
                return redirect('travel:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('travel:register')
            else:
                user = User.objects.create_user(username=uname, password=password, first_name=fname, last_name=lname,
                                                email=email)
                user.save()


        else:
            messages.info(request, "passwords are not matching")
            return redirect('travel:register')

        return redirect('travel:login')
    return render(request, 'reg.html')

def login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        password=request.POST['password']
        u=auth.authenticate(username=uname,password=password)

        if u is not None:
            auth.login(request,u)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('travel:login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')






