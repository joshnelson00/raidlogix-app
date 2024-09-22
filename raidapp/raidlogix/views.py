from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateAccountForm, SignInForm, CreateProjectForm, AddRiskForm, AddActionForm, AddAssumptionForm, AddIssueForm, AddDecisionForm, AddDependencyForm, AddTagForm, ChangePasswordForm, EditProfileForm
from django.http import HttpResponseRedirect, HttpResponseForbidden

from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
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
            return redirect("projects")

        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            for error in form.non_field_errors():
                messages.error(request, error)
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
    # Query the user_projects model to get the project ids linked to the current user
    user_projects_list = user_projects.objects.filter(user=current_user)
    # Use these project ids to filter the projects
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
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")

    form = CreateProjectForm(instance=this_project)
    
    if request.method == 'POST':
        if 'delete_project' in request.POST:
            this_project.delete()
            return redirect('projects')
        
        form = CreateProjectForm(request.POST, instance=this_project)
        if form.is_valid():
            form.save()
            return redirect('view_project', pk)
        
    context = {
        'project': this_project,
        'form': form,
    }
    return render(request, "view_project.html", context=context)

@login_required
def add_risk(request, pk):
    this_project = get_object_or_404(project, pk=pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    form = AddRiskForm()
    current_user = request.user
    if request.method == 'POST':
        form = AddRiskForm(request.POST)
        if form.is_valid():
            new_risk = form.save(commit=False)
            new_risk.project = this_project
            new_risk.owner = current_user
            new_risk.save()
            return redirect('risks', pk)
        else:
            print(form.errors)

    context = {
        'form':form
    }
   
    return render(request, 'add_risk.html', context=context)

@login_required
def view_risk(request, project_pk, risk_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    this_risk = get_object_or_404(risk, pk=risk_pk, project=this_project)
    form = AddRiskForm(instance=this_risk)
    current_user = request.user

    risk_tags = RiskTags.objects.filter(risk=this_risk)

    if request.method == 'POST':

        if 'delete_risk' in request.POST:
            # Delete the project and redirect to a project list page or homepage
            this_risk.delete()
            return redirect('risks', project_pk=this_project.pk)
        
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
        'project': this_project,
        'form':form,
        'risk': this_risk,
        'risk_tags': risk_tags,

    }
   
    return render(request, 'view_risk.html', context=context)

@login_required
def risks(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    risks = risk.objects.filter(project=this_project)

    context = {
        'project': this_project,
        'risks': risks,
    }
    return render(request, "risk_list.html", context=context)

@login_required
def add_action(request, pk):
    this_project = get_object_or_404(project, pk=pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")

    form = AddActionForm()
    current_user = request.user
    if request.method == 'POST':
        form = AddActionForm(request.POST)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.project = this_project
            new_action.owner = current_user
            new_action.save()
            return redirect('actions', pk)
        else:
            print(form.errors)

    context = {
        'form':form
    }
   
    return render(request, 'add_action.html', context=context)


@login_required
def actions(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    actions = action.objects.filter(project=this_project)
    context = {
        'project': this_project,
        'actions': actions,
    }
    return render(request, "action_list.html", context=context)


@login_required
def view_action(request, project_pk, action_pk):

    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_action = get_object_or_404(action, pk=action_pk, project=this_project)
    form = AddActionForm(instance=this_action)
    current_user = request.user

    action_tags = ActionTags.objects.filter(action=this_action)

    if request.method == 'POST':

        if 'delete_action' in request.POST:
            # Delete the project and redirect to a project list page or homepage
            this_action.delete()
            return redirect('actions', project_pk=this_project.pk)
        
        form = AddActionForm(request.POST, instance=this_action)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.project = this_project
            new_action.owner = current_user.username
            new_action.save()

            return redirect('actions', project_pk)
        else:
            print(form.errors)

    context = {
        'project': this_project,
        'form':form,
        'action': this_action,
        'action_tags':action_tags,

    }
   
    return render(request, 'view_action.html', context=context)

@login_required
def add_assumption(request, pk):
    this_project = get_object_or_404(project, pk=pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    form = AddAssumptionForm()
    if request.method == 'POST':
        form = AddAssumptionForm(request.POST)
        if form.is_valid():
            new_assumption = form.save(commit=False)
            new_assumption.project = this_project
            new_assumption.save()
            return redirect('assumptions', pk)
        else:
            print(form.errors)

    context = {
        'form':form
    }
   
    return render(request, 'add_assumption.html', context=context)

@login_required
def assumptions(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    assumptions = assumption.objects.filter(project=this_project)

    context = {
        'project': this_project,
        'assumptions': assumptions,
    }
    return render(request, "assumption_list.html", context=context)

@login_required
def view_assumption(request, project_pk, assumption_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_assumption = get_object_or_404(assumption, pk=assumption_pk, project=this_project)
    form = AddAssumptionForm(instance=this_assumption)

    assumption_tags = AssumptionTags.objects.filter(assumption=this_assumption)

    if request.method == 'POST':
        if 'delete_assumption' in request.POST:
            # Delete the project and redirect to a project list page or homepage
            this_assumption.delete()
            return redirect('assumptions', project_pk=this_project.pk)
        form = AddAssumptionForm(request.POST, instance=this_assumption)
        if form.is_valid():
            new_assumption = form.save(commit=False)
            new_assumption.project = this_project
            new_assumption.save()

            return redirect('assumptions', project_pk)
        else:
            print(form.errors)
    context = {
        'project': this_project,
        'form':form,
        'assumption': this_assumption,
        'assumption_tags':assumption_tags,

    }
   
    return render(request, 'view_assumption.html', context=context)

@login_required
def add_issue(request, pk):

    this_project = get_object_or_404(project, pk=pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    current_user = request.user
    form = AddIssueForm()
    if request.method == 'POST':
        form = AddIssueForm(request.POST)
        if form.is_valid():
            new_issue = form.save(commit=False)
            new_issue.project = this_project
            new_issue.owner = current_user
            new_issue.save()
            return redirect('issues', pk)
        else:
            print(form.errors)

    context = {
        'form':form,
    }
   
    return render(request, 'add_issue.html', context=context)

@login_required
def view_issue(request, project_pk, issue_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_issue = get_object_or_404(issue, pk=issue_pk, project=this_project)
    form = AddIssueForm(instance=this_issue)
    current_user = request.user

    issue_tags = IssueTags.objects.filter(issue=this_issue)

    if request.method == 'POST':
        if 'delete_issue' in request.POST:
            # Delete the project and redirect to a project list page or homepage
            this_issue.delete()
            return redirect('issues', project_pk=this_project.pk)
        form = AddIssueForm(request.POST, instance=this_issue)
        if form.is_valid():
            new_issue = form.save(commit=False)
            new_issue.project = this_project
            new_issue.owner = current_user.username
            new_issue.save()
            return redirect('issues', project_pk)
        else:
            print(form.errors)

    context = {
        'project': this_project,
        'form':form,
        'issue': this_issue,
        'issue_tags':issue_tags,

    }
   
    return render(request, 'view_issue.html', context=context)

@login_required
def issues(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    issues = issue.objects.filter(project=this_project)

    context = {
        'project': this_project,
        'issues': issues,
    }
    return render(request, "issue_list.html", context=context)

@login_required
def add_decision(request, pk):
    this_project = get_object_or_404(project, pk=pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    form = AddDecisionForm()
    if request.method == 'POST':
        form = AddDecisionForm(request.POST)
        if form.is_valid():
            new_decision = form.save(commit=False)
            new_decision.project = this_project
            new_decision.save()

            return redirect('decisions', pk)
        else:
            print(form.errors)

    context = {
        'form':form,
    }
   
    return render(request, 'add_decision.html', context=context)


@login_required
def decisions(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    decisions = decision.objects.filter(project=this_project)

    context = {
        'project': this_project,
        'decisions': decisions,
    }
    return render(request, "decision_list.html", context=context)


@login_required
def view_decision(request, project_pk, decision_pk):

    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_decision = get_object_or_404(decision, pk=decision_pk, project=this_project)
    form = AddDecisionForm(instance=this_decision)

    decision_tags = DecisionTags.objects.filter(decision=this_decision)

    if request.method == 'POST':
        if 'delete_decision' in request.POST:
            # Delete the project and redirect to a project list page or homepage
            this_decision.delete()
            return redirect('decisions', project_pk=this_project.pk)
        form = AddDecisionForm(request.POST, instance=this_decision)
        if form.is_valid():
            new_decision = form.save(commit=False)
            new_decision.project = this_project
            new_decision.save()
            return redirect('decisions', project_pk)
        else:
            print(form.errors)

    context = {
        'project': this_project,
        'form':form,
        'decision': this_decision,
        'decision_tags':decision_tags,

    }
   
    return render(request, 'view_decision.html', context=context)

@login_required
def add_dependency(request, pk):

    this_project = get_object_or_404(project, pk=pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    form = AddDependencyForm()
    if request.method == 'POST':
        form = AddDependencyForm(request.POST)
        if form.is_valid():
            new_dependency = form.save(commit=False)
            new_dependency.project = this_project
            new_dependency.save()
            return redirect('dependencies', pk)
        else:
            print(form.errors)

    context = {
        'form':form,
    }
   
    return render(request, 'add_dependency.html', context=context)

@login_required
def dependencies(request, project_pk):
    
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    dependencies = dependency.objects.filter(project=this_project)

    context = {
        'project': this_project,
        'dependencies': dependencies,
    }
    return render(request, "dependency_list.html", context=context)


@login_required
def view_dependency(request, project_pk, dependency_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_dependency = get_object_or_404(dependency, pk=dependency_pk, project=this_project)
    form = AddDependencyForm(instance=this_dependency)

    dependency_tags = DependencyTags.objects.filter(dependency=this_dependency)

    if request.method == 'POST':
        if 'delete_dependency' in request.POST:
            this_dependency.delete()
            return redirect('dependencies', project_pk=this_project.pk)
        
        form = AddDependencyForm(request.POST, instance=this_dependency)

        if form.is_valid():
            new_dependency = form.save(commit=False)
            new_dependency.project = this_project
            new_dependency.save()
            return redirect('dependencies', project_pk)
        else:
            print(form.errors)

    context = {
        'project': this_project,
        'form':form,
        'dependency': this_dependency,
        'dependency_tags':dependency_tags,

    }
   
    return render(request, 'view_dependency.html', context=context)


@login_required
def profile(request):
    current_user = request.user


    context = {
        'user':current_user,
    }
    return render(request, "profile.html", context=context)


@login_required
def tags(request, project_pk):

    this_project = get_object_or_404(project, pk=project_pk)
    tags = tag.objects.filter(project=this_project)
    
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    context = {
        'tags':tags, 
        'project':this_project,
    }
    return render(request, 'tag_list.html', context=context)




@login_required
def add_tag(request, project_pk):
    form = AddTagForm()
    this_project = get_object_or_404(project, pk=project_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    if request.method == 'POST':
        form = AddTagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.project = this_project
            tag.save()
            
            return redirect('tags', project_pk)
        else:
            print(form.errors)

    context = {
        'form':form,
        'project':this_project
    }

    return render(request, 'add_tag.html', context=context)

@login_required
def view_tag(request, project_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)
    form = AddTagForm(instance=this_tag)

    if request.method == 'POST':
        if 'delete_tag' in request.POST:
            this_tag.delete()
            return redirect('tags', project_pk=this_project.pk)
        
        form = AddTagForm(request.POST, instance=this_tag)

        if form.is_valid():
            new_tag = form.save(commit=False)
            new_tag.project = this_project
            new_tag.save()
            return redirect('tags', project_pk)
        else:
            print(form.errors)

    context = {
        'form':form,
    }
   
    return render(request, 'view_tag.html', context=context)

@login_required
def profile(request):
    user = request.user
    date_created = user.date_joined

    context = {
        'date_created': date_created
    }
    return render(request, 'profile_settings.html', context=context)

@login_required
def change_user_info(request):
    current_user = request.user
    form = EditProfileForm(instance=current_user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    context = {
        'form':form
    }
    return render(request, 'edit_profile.html', context=context)

@login_required
def change_password(request):

    current_user = request.user
    form = ChangePasswordForm(user=current_user)
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=current_user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            for error in form.non_field_errors():
                messages.error(request, error)
    context = {
        'form':form
    }
    return render(request, 'change_password.html', context=context)

@login_required
def risk_tags(request, project_pk, risk_pk):

    this_project = get_object_or_404(project, pk=project_pk)

    tags = tag.objects.filter(project=this_project)

    this_risk = get_object_or_404(risk, pk=risk_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    


    context = {
        'tags':tags, 
        'project':this_project,
        'risk':this_risk,
    }

    return render(request, 'attach_risk_tag.html', context=context)



@login_required
def action_tags(request, project_pk, action_pk):

    this_project = get_object_or_404(project, pk=project_pk)

    tags = tag.objects.filter(project=this_project)

    this_action = get_object_or_404(action, pk=action_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    


    context = {
        'tags':tags, 
        'project':this_project,
        'action':this_action,
    }

    return render(request, 'attach_action_tag.html', context=context)

@login_required
def assumption_tags(request, project_pk, assumption_pk):

    this_project = get_object_or_404(project, pk=project_pk)

    tags = tag.objects.filter(project=this_project)

    this_assumption = get_object_or_404(assumption, pk=assumption_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    


    context = {
        'tags':tags, 
        'project':this_project,
        'assumption':this_assumption,
    }

    return render(request, 'attach_assumption_tag.html', context=context)

@login_required
def issue_tags(request, project_pk, issue_pk):

    this_project = get_object_or_404(project, pk=project_pk)

    tags = tag.objects.filter(project=this_project)

    this_issue = get_object_or_404(issue, pk=issue_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    


    context = {
        'tags':tags, 
        'project':this_project,
        'issue':this_issue,
    }

    return render(request, 'attach_issue_tag.html', context=context)

@login_required
def decision_tags(request, project_pk, decision_pk):

    this_project = get_object_or_404(project, pk=project_pk)

    tags = tag.objects.filter(project=this_project)

    this_decision = get_object_or_404(decision, pk=decision_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    


    context = {
        'tags':tags, 
        'project':this_project,
        'decision':this_decision,
    }

    return render(request, 'attach_decision_tag.html', context=context)

@login_required
def dependency_tags(request, project_pk, dependency_pk):

    this_project = get_object_or_404(project, pk=project_pk)

    tags = tag.objects.filter(project=this_project)

    this_dependency = get_object_or_404(dependency, pk=dependency_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    


    context = {
        'tags':tags, 
        'project':this_project,
        'dependency':this_dependency,
    }

    return render(request, 'attach_dependency_tag.html', context=context)



















@login_required
def risk_attach_tag(request, project_pk, risk_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)
    

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_risk = get_object_or_404(risk, pk=risk_pk, project=this_project)
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)

    new_risk_tag = RiskTags(tag=this_tag, risk=this_risk)
    new_risk_tag.save()


    form = AddRiskForm(instance=this_risk)

    

    return redirect('view_risk', project_pk=project_pk, risk_pk=risk_pk)

@login_required
def action_attach_tag(request, project_pk, action_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_action = get_object_or_404(action, pk=action_pk, project=this_project)
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)

    new_action_tag = ActionTags(tag=this_tag, action=this_action)
    new_action_tag.save()

    form = AddActionForm(instance=this_action)

    return redirect('view_action', project_pk=project_pk, action_pk=action_pk)

@login_required
def assumption_attach_tag(request, project_pk, assumption_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_assumption = get_object_or_404(assumption, pk=assumption_pk, project=this_project)
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)

    new_assumption_tag = AssumptionTags(tag=this_tag, assumption=this_assumption)
    new_assumption_tag.save()

    form = AddAssumptionForm(instance=this_assumption)

    return redirect('view_assumption', project_pk=project_pk, assumption_pk=assumption_pk)

@login_required
def issue_attach_tag(request, project_pk, issue_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_issue = get_object_or_404(issue, pk=issue_pk, project=this_project)
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)

    new_issue_tag = IssueTags(tag=this_tag, issue=this_issue)
    new_issue_tag.save()

    form = AddIssueForm(instance=this_issue)

    return redirect('view_issue', project_pk=project_pk, issue_pk=issue_pk)

@login_required
def decision_attach_tag(request, project_pk, decision_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_decision = get_object_or_404(decision, pk=decision_pk, project=this_project)
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)

    new_decision_tag = DecisionTags(tag=this_tag, decision=this_decision)
    new_decision_tag.save()

    form = AddDecisionForm(instance=this_decision)

    return redirect('view_decision', project_pk=project_pk, decision_pk=decision_pk)

@login_required
def dependency_attach_tag(request, project_pk, dependency_pk, tag_pk):
    this_project = get_object_or_404(project, pk=project_pk)

    if not user_projects.objects.filter(user=request.user, project=this_project).exists():
        return HttpResponseForbidden("You do not have permission to access this project.")
    
    this_dependency = get_object_or_404(dependency, pk=dependency_pk, project=this_project)
    this_tag = get_object_or_404(tag, pk=tag_pk, project=this_project)

    new_dependency_tag = DependencyTags(tag=this_tag, dependency=this_dependency)
    new_dependency_tag.save()

    form = AddDependencyForm(instance=this_dependency)

    return redirect('view_dependency', project_pk=project_pk, dependency_pk=dependency_pk)




