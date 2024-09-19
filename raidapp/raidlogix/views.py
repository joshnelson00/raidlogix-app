from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateAccountForm, SignInForm, CreateProjectForm, AddRiskForm, AddActionForm
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
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
                return redirect("projects")
    context = {
        'form':form
    }
    return render(request, 'sign_in.html', context=context)

@login_required
def sign_out(request):
    auth.logout(request)
    return redirect("login")

@login_required
def projects(request):
    current_user = request.user
    user_projects_list = user_projects.objects.filter(user=current_user)
    projects = project.objects.filter(id__in=user_projects_list.values_list('project_id', flat=True))
    context = {
        'projects': projects,
        'user': current_user,
    }

    return render(request, 'project_list.html', context)

@login_required
def create_project(request):
    form = CreateProjectForm()
    current_user = request.user
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save()
            
            # Create a new user_projects entry
            new_user_project = user_projects(user=current_user, project=new_project)
            new_user_project.save()
            
            return redirect("projects")
        


    context = {
        'form': form
    }
    return render(request, 'create_project.html',context=context)


@login_required
def view_project(request, pk):
    
    this_project = get_object_or_404(project, pk=pk)
    form = CreateProjectForm(instance=this_project)
    risks = risk.objects.filter(project=this_project)

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, instance=this_project)
        if form.is_valid():
            form.save()
            return redirect('view_project', pk)
    context = {
        'project': this_project,
        'form': form,
        'risks': risks,
    }
    return render(request, "view_project.html", context=context)

@login_required
def add_risk(request, pk):
    this_project = get_object_or_404(project, pk=pk)
    form = AddRiskForm()
    current_user = request.user
    if request.method == 'POST':
        form = AddRiskForm(request.POST)
        if form.is_valid():
            new_risk = form.save(commit=False)
            new_risk.project = this_project
            new_risk.owner = current_user
            new_risk.save()
            return redirect('view_project', pk)
        else:
            print(form.errors)

    context = {
        'form':form
    }
   
    return render(request, 'add_risk.html', context=context)

@login_required
def view_risk(request, project_pk, risk_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    this_risk = get_object_or_404(risk, pk=risk_pk, project=this_project)
    form = AddRiskForm(instance=this_risk)
    current_user = request.user

    if request.method == 'POST':
        form = AddRiskForm(request.POST, instance=this_risk)
        if form.is_valid():
            new_risk = form.save(commit=False)
            new_risk.project = this_project
            new_risk.owner = current_user.username
            new_risk.save()
            return redirect('risks', project_pk)
        else:
            print(form.errors)
            
    context = {
        'form':form,

    }
   
    return render(request, 'view_risk.html', context=context)

@login_required
def risks(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    risks = risk.objects.filter(project=this_project)

    context = {
        'project': this_project,
        'risks': risks,
    }
    return render(request, "risk_list.html", context=context)

@login_required
def add_action(request, pk):
    this_project = get_object_or_404(project, pk=pk)
    form = AddActionForm()
    current_user = request.user
    if request.method == 'POST':
        form = AddActionForm(request.POST)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.project = this_project
            new_action.owner = current_user
            new_action.save()

            return redirect('view_project', pk)
        else:
            print(form.errors)

    context = {
        'form':form
    }
   
    return render(request, 'add_action.html', context=context)


@login_required
def actions(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    actions = action.objects.filter(project=this_project)
    context = {
        'project': this_project,
        'actions': actions,
    }
    return render(request, "action_list.html", context=context)

@login_required
def view_action(request, project_pk, action_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    this_action = get_object_or_404(action, pk=action_pk, project=this_project)
    form = AddActionForm(instance=this_action)
    current_user = request.user

    if request.method == 'POST':
        form = AddActionForm(request.POST, instance=this_action)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.project = this_project
            new_action.owner = current_user.username
            new_action.save()

            return redirect('view_project', project_pk)
        else:
            print(form.errors)

    context = {
        'form':form
    }
   
    return render(request, 'view_action.html', context=context)



