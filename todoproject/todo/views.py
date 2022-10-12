from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import tform
from .models import todo
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class dlw(DeleteView):
    model=todo
    template_name = 'del.html'
    success_url = reverse_lazy('cbvhome')

class uw(UpdateView):
    model= todo
    template_name = 'update.html'
    context_object_name = 't'
    fields = ('task','prio','date')

class dw(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 't'

class lw(ListView):
    model=todo
    template_name = 'home.html'
    context_object_name = 't'


# Create your views here.


def home(request):
    t=todo.objects.all()
    if request.method=='POST':
       task=request.POST.get('task')
       prio=request.POST.get('prio')
       date=request.POST.get('date')
       # if User.objects.filter(prio=prio).exists():
       #     messages.info(request, "priority is already given")
       #     return redirect('/')
       # else:
       td = todo(task=task, prio=prio,date=date)
       td.save()
       #     messages.info(request, "Task successfully added")
       # return redirect('/')
    return render(request,'home.html',{'t':t})
def delete(request,id):
    t=todo.objects.get(id=id)
    if request.method=='POST':
        t.delete()
        return redirect('/')
    return render(request,'del.html')
def edit(request,id):
    t=todo.objects.get(id=id)
    form=tform(request.POST or None,request.FILES,instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'t':t})


