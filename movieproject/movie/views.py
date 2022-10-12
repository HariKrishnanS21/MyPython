from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import movform
from . models import movie
from django.contrib import messages

# Create your views here.
def home(request):
    mov=movie.objects.all()
    return render(request,'home.html',{'mov_list':mov})
def detail(request,mov_id):
    mov=movie.objects.get(id=mov_id)
    return render(request,'detail.html',{'mov':mov})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        pic=request.FILES['pic']
        mov=movie(name=name,desc=desc,year=year,pic=pic)
        mov.save()
    return render(request,'add.html')
def edit(request,id):
    mov=movie.objects.get(id=id)
    form=movform(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mov':mov})
def delete(request,id):
    mov=movie.objects.get(id=id)
    if request.method=='POST':
        mov.delete()
        return redirect('/')
    return render(request,'del.html')
