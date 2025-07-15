from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import logout


def register(request):
    if request.method=="POST":
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"New User Registered, Login To Get Started")
            return redirect('register')
    else:
        register_form=CustomRegisterForm()
    return render(request,'register.html',{'form':register_form})

def logout_view(request):
    logout(request)
    return redirect('login')



    