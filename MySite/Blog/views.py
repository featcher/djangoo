from django.contrib.auth import logout
from django.shortcuts import render,redirect
from Blog.models import user
from Blog.forms import details,one,gin,new

# Create your views here.
def col(request):
    if request.method=="POST":
        form=details(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'user.html')
def home(request):
    return render(request,'home.html')

def fir(request):
    if request.method=="POST":
        form=one(request.POST)
        if form.is_valid:
            form.save()
    return render(request,'first.html')

def loo(request):
    return render(request, 'base.html')

def dis(request):
    return render(request,'disc.html')

def foo(request):
    return render(request,'food.html')

def gam(request):
    return render(request,'game.html')

def mus(request):
    return render(request,'music.html')

def ran(request):
    return render(request,'rand.html')

def logg(request):
    if request.method=="POST":
        form=gin(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home2')
    return render(request,'login.html')
def home2(request):
    return render(request,'home2.html')

def cre(request):
    # if request.method=="POST":
    #     form=new(request.POST)
    #     if form.is_valid:
    #         form.save()
    return render(request,'create.html')

def upd(request):
    if request.method == 'POST':
        user = request.details
        username = request.POST['username']
        email = request.POST['email']
        bio = request.POST['bio']
        details.username = username
        details.email = email
        details.bio = bio
        details.save()
        return redirect('profile')
    return render(request, 'profile.html')

def logu(request):
    return redirect('login.html')
def showlog(request):
    return render(request,'logout.html')
def bl1(request):
    return render(request,'blog1.html')
def bl2(request):
    return render(request,'blog2.html')