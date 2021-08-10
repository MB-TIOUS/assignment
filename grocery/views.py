from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import os
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from grocery.models import list_element as le
# Create your views here.

def index(request):
    try:
        if 'username' in request.session:
            return redirect('view_list')

        elif request.method == "POST":
            username = request.POST.get('username').strip()
            password = request.POST.get('password')
            user =  auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                request.session['username'] = username
                messages.success(request, 'Login successfully.')
                return redirect('view_list')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request,'index.html')
        else:
            
            return render(request,'index.html')
    except Exception as e:
        print(e)
        messages.error(request, 'Please login again')
        return render(request,'index.html')

def signup(request):
    try:
        if request.method == "POST":
            username = (request.POST.get('username')).strip()
            email = (request.POST.get('email')).strip()
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken.')
                return render(request,'sign.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email is already registered.')
                return render(request,'sign.html')
            elif len(username)==0:
                messages.error(request, 'enter valid username')
                return render(request,'sign.html')
            else:
                user =  User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request, 'Profile successfully created.')
                return redirect('/')

        else:
            return render(request,'sign.html')
    except Exception as e:
        messages.error(request, 'Please sign up again')
        return render(request,'sign.html')

def logout(request):
    auth.logout(request)
    request.session.flush()
    request.session.clear_expired()
    return redirect('/')

def view_list(request):
    if 'username' in request.session:
        list_obj = le.objects.filter(un=request.session['username'])
        return render(request,'view.html',{'list_obj':list_obj})
    else:
        return redirect('/')

def add_list(request):
    if 'username' in request.session:
        if request.method =="POST":
            un = request.session['username']
            name = request.POST.get('in')
            quantity = request.POST.get('iq')
            status = request.POST.get('is')
            idate = request.POST.get('idate')

            obj = le(un=un,iname=name,iquantity=quantity,istatus=status,idate=idate)
            obj.save()

            return redirect('view_list')
        else:
            return render(request,'add.html')
    else:
        return redirect('/')

def update_list(request,id):
    if 'username' in request.session:
        if request.method =="POST":
            obj = le.objects.filter(id=id).first()
            obj.iname = request.POST.get('in')
            obj.iquantity = request.POST.get('iq')
            obj.istatus = request.POST.get('is')
            obj.idate = request.POST.get('idate')
            obj.save()
            return redirect('view_list')
        else:
            return render(request,'update.html',{'id':id})
    else:
        return redirect('/')

def list_delete(request,id):
    if 'username' in request.session:
        obj = le.objects.filter(id=id)
        obj.delete()
        return redirect('view_list')
    else:
        return redirect('/')