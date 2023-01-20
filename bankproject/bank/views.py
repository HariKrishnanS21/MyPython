from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import pdet


# Create your views here.
def home(request):
    return render(request,'home.html')

def forms(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        mob=request.POST['mob']
        mail=request.POST['mail']
        address=request.POST['address']
        person=pdet(name=name,dob=dob,age=age,mob=mob,mail=mail,address=address)
        person.save()
        messages.info(request,"information added successfully")
        return redirect('bank:forms')
    return render(request,'forms.html')

# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request,'forms.html', {'form': form})
#
# def load_branches(request):
#     district_id = request.GET.get('district_id')
#     branch = branches.objects.filter(district_id=district_id).all()
#     return render(request, 'branch_list.html', {'branch': branch})

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        u=auth.authenticate(username=username,password=password)

        if u is not None:
            auth.login(request,u)
            return redirect('bank:forms')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('bank:login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        uname=request.POST['uname']
        password=request.POST['pass']
        cpass=request.POST['cpass']

        if password == cpass:
            if User.objects.filter(username=uname):
                print("username")
                # messages.info(request,"Username already exist")
                return redirect('bank:register')
            else:
                user=User.objects.create_user(username=uname,password=password)
                user.save()
                print("user")
                # messages.info(request,"user successfully created")
        else:
            print("pass")
            # messages.info(request,"passwords are not  matching")
            return redirect('bank:register')
        return redirect('bank:login')

    return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('/')