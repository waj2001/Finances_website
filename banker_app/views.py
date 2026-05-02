from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.paginator import Paginator
from math import *
from django.contrib import  messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.



def home(request):
    df = Employee.objects.all().order_by('id')
    df_pageginatore = Paginator(df,3)
    pagenum = request.GET.get('page')
    page = df_pageginatore.get_page(pagenum)
    context = {'page':page,
    'total_No_page':ceil(df_pageginatore.count/3),
    'total_No_Data': ceil(df_pageginatore.count)
               }


    return render(request,"index.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use renamed login function to avoid conflict
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'signin.html')
  

def signup_view(request):

    if request.method == 'POST':
       First_name = request.POST['First_name']
       Last_name = request.POST['Last_name'] 
       username = request.POST['username'] 
       Email = request.POST['Email'] 
       Password1 = request.POST['Password1'] 
       Password2 = request.POST['Password2']
       
       
       if Password1 == Password2:

             if User.objects.filter(email = Email).exists():
                messages.info(request,"Email Allready Used by Another one")
                return redirect("signup")
             elif User.objects.filter(username=username).exists():
                messages.info(request,"User Allready used by another one")
                return redirect("signup")
             else:
                user = User.objects.create_user(first_name = First_name, last_name = Last_name, username=username, email = Email)
                user.save()
                return redirect("signin") 

       else:
            messages.info(request,"Didn't Match both password, Something went wrong")
            return redirect("signup")
       
    return render(request,"signup.html")

def signout(request):
    logout(request)
    return redirect("/")

def calculation(request):
    return render(request,"calc.html")


def add(request):
    n1=int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    df=n1+n2
    return render(request,"result.html",{"data":df})

def sub(request):
    n1=int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    df=n1-n2
    return render(request,"result.html",{"data":df})

def mult(request):
    n1=int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    df=n1*n2
    return render(request,"result.html",{"data":df})

def div(request):
    n1=int(request.POST["num1"])
    n2 = int(request.POST["num2"])
    df=n1/n2
    return render(request,"result.html",{"data":df})

def banker(request):
    return HttpResponse("This is Finances website")