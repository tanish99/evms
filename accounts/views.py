from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from evmsmod.models import Data,Doctor
from django.contrib import messages
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import View
from accounts.utils import *
import datetime
    
user=None
def register(request):
    if request.method=='POST':
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        if password ==cpassword:
            if Data.objects.filter(email=email).exists():
                 messages.info(request,'email taken')
            
           
            
            else:
                user=User.objects.create_user(username=email,first_name=fn,last_name=ln,email=email,password=password)
                user.save();
                print("created")
                messages.info(request,'registration successfull')
        else:
            messages.info(request,'passwords dont match')
        return render(request,"register.html")
        
        
    else:
        return render(request,"register.html")
    
    pass
c=None
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        global user
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            
            if user.is_staff:
                auth.login(request,user)
                return render(request,'index.html')

                
                
            else:
                 
                 auth.login(request,user)
                 
               
                 
                 return render(request,'index.html')
                
                 

        else:
            return render(request,"login.html")
    else:
        return render(request,'login.html')

    
    pass
def logout(request):
    auth.logout(request)
    return redirect("/")
def getdata(request):
    
    if request.method=='POST':
        id=request.POST['pat_detail']
        name=request.POST['full_name']
        weight=request.POST['weight']
        bp=request.POST['BP']
        bg=request.POST['BG']
        pd=request.POST['pd']
        diag=request.POST['diag']
        pres=request.POST['pre']
        d=Doctor(int(id),name,float(weight),bp,bg,pd,diag,pres)
        d.save();
    return redirect("/")
    pass


def dul(request):
    patients = User.objects.values_list('id')
    auth.login(request,user)
    return render(request,'doctor_login.html',{'data':patients})

def vd(request):
      
      u=int(user.id)
      print(u)
      if(Doctor.objects.filter(id=u).exists()):
        global c   
        c=Doctor.objects.get(id=u)
        return render(request,'patient_login.html',{'det':c})
      else:
        return HttpResponse("<h1>details  not yet recieved<h1>")


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('simple.html')
        context = {

        }
        html = template.render({'det':c})
        print(c)
        pdf = render_to_pdf('simple.html',{'det':c})
        

        
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "prescription_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
def ba(request):
    return HttpResponse("<h1>this page is still under construction<h1>")

