from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=50)
    due = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.TextField()


    #FIX RIGHT HERE
class tag(models.Model):
    tag_name = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)


class issue(models.Model):
    created = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    description = models.TextField()
    impact_details = models.TextField()
    #raised/monitoring/closed/converted to an issue
    state = models.CharField(max_length=50)
    #integer between 1-100
    importance = models.IntegerField()
    #integer between 1-100
    impact = models.IntegerField()
    response_status = models.TextField()
    resolution = models.TextField()
    date_resolved = models.CharField(max_length=50)
    root_cause = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class action(models.Model):
    created = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.CharField(max_length=50)
    #created/assigned/in work/in review/done/draft/on hold/delegated/blocked (waiting internal)/blocked (waiting external)
    state = models.CharField(max_length=50)
    action_source = models.CharField(max_length=50)
    importance = models.IntegerField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class decision(models.Model):
    created = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    due = models.CharField(max_length=50)
    #created/decided/in review/draft/deferred
    state = models.CharField(max_length=50)
    #created/decided/in review/draft/deferred
    decision_made = models.CharField(max_length=50)
    justification = models.TextField()
    impact = models.TextField()
    #integer between 1-100
    importance = models.IntegerField()
    project = models.ForeignKey(project, on_delete = models.CASCADE)

class assumption(models.Model):
    created = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    item = models.TextField()
    notes = models.TextField()
    project = models.ForeignKey(project, on_delete = models.CASCADE)

class risk(models.Model):
    created = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.CharField(max_length=50)
    #raised/monitoring/closed/converted to an issue
    state = models.CharField(max_length=50)
    #integer between 1-100
    probability = models.IntegerField()
    #integer between 1-100
    impact = models.IntegerField()
    #score = (probability * impact) DOUBLE CHECK HERE
    score = models.DecimalField(decimal_places=2, max_digits=5)
    date_raised = models.CharField(max_length=50)
    trigger_date = models.CharField(max_length=50)
    date_closed = models.CharField(max_length=50)
    #avoice, mitigate, transfer, accept, escalate
    response_strategy = models.CharField(max_length=50)
    #red (behind), amber (in progress), green (on-track)
    response_plan_state = models.CharField(max_length=50)
    project = models.ForeignKey(project, on_delete = models.CASCADE)

class dependency(models.Model):
    name = models.CharField(max_length=50)
    due = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.CharField(max_length=50)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class user_projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)



class IssueTags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    issue = models.ForeignKey(issue, on_delete=models.CASCADE)

class ActionTags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    action = models.ForeignKey(action, on_delete=models.CASCADE)

class DecisionTags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    decision = models.ForeignKey(decision, on_delete=models.CASCADE)

class AssumptionTags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    assumption = models.ForeignKey(assumption, on_delete=models.CASCADE)

class RiskTags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    risk = models.ForeignKey(risk, on_delete=models.CASCADE)

class DependencyTags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    dependency = models.ForeignKey(dependency, on_delete=models.CASCADE)




    
    
    


