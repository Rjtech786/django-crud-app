from concurrent.futures import process
from multiprocessing import context
from turtle import textinput
from unittest import result
from django.shortcuts import render,HttpResponse, HttpResponseRedirect ,redirect
from projectapp.models import Employees
def translate(request):
    result="" 
    a=""
    if request.method=="POST":
        a=request.POST.get('text')
        b=request.POST.get('lang')
        translator = Translator()
        process = translator.translate(a, src='en', dest=b)
        result =process.text 
    else:
        pass
    return render (request, "translate.html" , {'text':a, 'output':result} )

def index(request):
  emp=Employees.objects.all()
  
  context={
      'emp':emp,
      }
  return render (request,'login.html',context)

   
def add(request):
    if request.method == 'POST':
        field_name= request.POST.get('name')
        field_rollno= request.POST.get('rollno')
        field_email= request.POST.get('email')  
        field_address= request.POST.get('address')  
        field_phone= request.POST.get('phone')  
        new = Employees(name=field_name,rollno=field_rollno,email=field_email,address=field_address,phone=field_phone) 
        new.save()
        print ("add")
        return redirect('home')
    return render(request, 'login.html')

def edit(request):
  emp = Employees.objects.all()
  context= {
     'emp':emp,
  }
  return redirect(request,'login.html',context)

def update(request,id):
   if request.method=="POST":
      name = request.POST.get('name1')
      rollno = request.POST.get('rollno1')
      email = request.POST.get('email2')
      address = request.POST.get('address3')
      phone = request.POST.get('phone4')
      em= Employees (
         id=id,
         name=name,
         rollno=rollno,
         email=email,
         address=address,
         phone = phone,
      )
      em.save()
      print("updated")
      return redirect('/')
   return render(request,"login.html")


def delete(request,id):
   emp= Employees.objects.filter(id=id)
   emp.delete()
   context={
      'emp':emp,
   }
   return redirect('home')
