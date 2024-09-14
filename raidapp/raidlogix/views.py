from django.shortcuts import render, redirect
from .forms import CreateAccountForm, SignInForm, CreateProjectForm
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def template(request):
    return render(request, "h_and_f.html")

@login_required
def home(request):
    return render(request, "home.html")
def login(request):
    return render(request, "landing.html")

def create_account(request):
    form = CreateAccountForm()
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form':form}

    return render(request, 'create_account.html', context=context)


def sign_in(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:

                auth.login(request, user)
                return redirect("home")
    context = {
        'form':form
    }
    return render(request, 'sign_in.html', context=context)


def sign_out(request):
    auth.logout(request)
    return redirect("login")

@login_required
def projects(request):

    context = {
        
    }
    return render(request, 'project_list.html', context)

def create_project(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        'form': form
    }
    return render(request, 'create_project.html',context=context)