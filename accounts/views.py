from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def signup(request):
    if request.method=='POST':
        try:
            unm=request.POST['username']
            phone=request.POST['phone']
            email=request.POST['email']
            password=request.POST['pass']
            login=Login(username=unm,password=password)
            login.save()
            data=Signup(username=unm,phone=phone,email=email,password=password,login=login)
            data.save();
            return render(request,'signup.html',{'success':'registered'})
            # return HttpResponse("success")
            # return redirect('/login')
        except Exception as err: 
            return HttpResponse(err)
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        try:
            un=request.POST['username']
            pw=request.POST['pass']
            user=Login.objects.get(username=un,password=pw)
            request.session['log_id']=user.id
            # return render(request,'profile.html',{'user':user})
            # return HttpResponse("logi suceesss")
            return redirect('/profile')
        except:
            return HttpResponse("logi un  nnn suceesss")
    else:
        return render(request, 'login.html')

def profile(request):
    user_id=request.session['log_id']
    print(user_id)
    user_data=Signup.objects.get(login=user_id)
    # print(email)
    return render(request,'profile.html',{'user':user_data})


