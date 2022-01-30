from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from .models import Club

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        un=request.user.username
        user=User.objects.filter(username=un)[0]
        if user is not None and user.is_superuser:
            clubname=Club.objects.filter(president_username=un)[0].name
            return HttpResponseRedirect(reverse('svceClubMgmtApp:presidenthome',kwargs={'nm':clubname}))
    clublist=Club.objects.all()
    return render(request,'index.html',{'clublist':clublist})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return HttpResponseRedirect('login')
    return render(request,'register.html')

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            un = request.POST['username']
            pass1 = request.POST['pass1']
            print(un,pass1)
            user=User.objects.filter(username=un)
            if len(user)==1:
                if check_password(pass1,user[0].password):
                    user = authenticate(username=un,password=pass1)
                    print(user)
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse('svceClubMgmtApp:index'))
                    else:
                        print('username or password is wrong')
                        return HttpResponseRedirect('login')
            else:
                print('username or password is wrong')
                return HttpResponseRedirect('login')        
        return render(request, "login.html")
    else:
        return HttpResponseRedirect(reverse('svceClubMgmtApp:index'))

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('svceClubMgmtApp:index'))

def club(request,nm):
    clublist=Club.objects.filter(name=nm)[0]
    print(clublist)
    about=clublist.about
    about_list=about.split('<br>')
    clublist.about=about_list
    return render(request,'clubpage.html',{'clublist':clublist})

def actrec(request,nm):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            club=Club.objects.filter(name=nm)[0]
            username=club.president_username
            if request.user.username==username:
                club.recruiting=1
                club.save()
                return HttpResponseRedirect(reverse('svceClubMgmtApp:clubPage',kwargs={'nm':nm}))
            else:return HttpResponse('access denied!')
        else:return HttpRequest('dont have access for students!')
    else:
        return HttpResponseRedirect(reverse('svceClubMgmtApp:index'))


