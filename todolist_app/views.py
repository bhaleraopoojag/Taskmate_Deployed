from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import tasklistmodel,contactmodel
from todolist_app.forms import taskform,contactform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"index.html")
    
@login_required
def todolist(request):
    if request.method=="POST":
        form=taskform(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage_id=request.user
            instance.save()
            messages.success(request,'New Data Saved!!')
        return redirect('todolist')
    else:
        all_task=tasklistmodel.objects.filter(manage_id=request.user)
        paginator=Paginator(all_task,5)
        page=request.GET.get('pg')
        all_task=paginator.get_page(page)
    return render(request,"todolist.html",{'objects':all_task})

def editTask(request,taskid):
    if request.method=="POST":
        taskiee=tasklistmodel.objects.get(pk=taskid)
        formobj=taskform(request.POST or None,instance=taskiee)
        if formobj.is_valid():
            formobj.save()
        messages.success(request,'Task Edited!!')
        return redirect('todolist')
    else:
        oneObj=tasklistmodel.objects.get(pk=taskid)
    return render(request,"edit.html",{'objects':oneObj})
    

def deleteTask(request,taskid):
    task=tasklistmodel.objects.get(pk=taskid)
    if task.manage_id == request.user:
        task.delete()
    else:
         messages.error(request,'Page Restricted!! for deletion')        
    
    return redirect('todolist')

def completestatus(request,taskid):
    task=tasklistmodel.objects.get(pk=taskid)
    if task.manage_id == request.user:
        task.done=True 
        task.save()
    else:
        messages.error(request,'Page Restricted!!')
    return redirect('todolist')

def pendingstatus(request,taskid):
    task=tasklistmodel.objects.get(pk=taskid)
    task.done=False
    task.save()
    return redirect('todolist')

def contact(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            contactmodel.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            # return redirect()
        # refresh your fileds after saving tha data in db
        form=contactform()
    else:
        form=contactform()
    return render(request,'contact.html',{'form':form})

def about(request):
    return render(request,'about.html')