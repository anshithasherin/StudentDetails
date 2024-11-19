

# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from students.forms import LoginForm,RegForm,StudentModelform
from django.contrib.auth import authenticate
from .models import Students
from django.contrib import messages

# Create your views here.
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{"form":form})
    def post(self,request):
        formdata=LoginForm(data=request.POST)
        if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return redirect('landing')
            else:
                return redirect('log')
        return render(request,'login.html',{"form":formdata})
    
    
class Landingview(View):
    def get(self,request):
        return render(request,'landing.html')
    
class RegView(View):
    def get(self,request):
        form=RegForm
        return render(request,'reg.html',{"form":form})
    def post(self,request,**kwargs):
        formdata=RegForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('log')
        return render(request,'reg.html',{'form':formdata})
    
class dashboardview(View):
    def get(self,request):
        data=Students.objects.all()
        return render(request,'dashboard.html',{"students":data})
    
class AddStudentDetailsview(View):
    def get(self,request):
        form=StudentModelform()
        return render(request,'adddetails.html',{"form":form})
    def post(self,request):
        formdata=StudentModelform(data=request.POST,files=request.FILES)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,'Details succesfully added!!')
    
            return redirect('dash')
        messages.error(request,'Invalid Data')
        return render(request,'dashboard.html',{'form':formdata})
    
class EditDetailsView(View):
     def get(self,request,**kwargs):
        sid=kwargs.get('id')
        student=Students.objects.get(id=sid)
        form=StudentModelform(instance=student)
        return render(request,'edit.html',{'form':form})
     def post(self,request,**kwargs):
        sid=kwargs.get('id')
        student=Students.objects.get(id=sid)
        formdata=StudentModelform(data=request.POST,files=request.FILES,instance=student)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,'Successfully Updated')
            return redirect('dash')
        return render(request,'edit.html',{"form":formdata})
     
class DeleteDetailsView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        print(id)
        student=Students.objects.get(id=pid)
        student.delete()
        messages.success(request,'Successfully Deleted')
        return redirect("dash")




