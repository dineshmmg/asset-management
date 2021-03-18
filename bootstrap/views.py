from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from manager.models import *
from django.contrib.auth.models import Group

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.
@login_required(login_url='login')
@admin_only
def index(request):
    main_infos = asset_types.objects.all()
    context={
        'main_infos': main_infos
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']   
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                group = Group.objects.get(name='user')
                user.groups.add(group)
                messages.info(request, 'User Created')
                return render(request,'login.html')
                
        else:
            messages.info(request, 'password not matching...')
            return redirect('register')
        
           
    else:
        return render(request, "register.html")
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request,'login.html')


def userpage(request):
    queryset = user_assets.objects.filter(user_id=request.user.id)
    context ={
        "queryset":queryset,
    }
    return render(request, 'user.html', context)
