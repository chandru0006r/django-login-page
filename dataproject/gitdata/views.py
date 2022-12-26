from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def home(request):
    return render(request,"gitpage/home.html")

@login_required(login_url='../accounts/login/')
def profile(request):
    return render(request,"gitpage/profile.html")

@permission_required('gitpage.view_staff',login_url='../accounts/login/')
def repository(request):
    return render(request,"gitpage/repository.html")