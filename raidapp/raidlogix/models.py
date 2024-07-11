from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=50)
    due = models.DateField()
    description = models.TextField()
    budget = models.FloatField()

class tag(models.Model):
    tag_name = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class employee(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class issue(models.Model):
    created = models.DateField()
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
    date_resolved = models.DateField()
    root_cause = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class action(models.Model):
    created = models.DateField()
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    #created/assigned/in work/in review/done/draft/on hold/delegated/blocked (waiting internal)/blocked (waiting external)
    state = models.CharField(max_length=50)
    action_source = models.CharField(max_length=50)
    importance = models.IntegerField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class decision(models.Model):
    created = models.DateField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    due = models.DateField()
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
    created = models.DateField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    updated = models.TextField()
    item = models.TextField()
    notes = models.TextField()
    project = models.ForeignKey(project, on_delete = models.CASCADE)

class risk(models.Model):
    created = models.DateField()
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
    score = models.IntegerField()
    date_raised = models.DateField()
    trigger_date = models.DateField()
    date_closed = models.DateField()
    #avoice, mitigate, transfer, accept, escalate
    response_strategy = models.CharField(max_length=50)
    #red (behind), amber (in progress), green (on-track)
    response_plan_state = models.CharField(max_length=50)
    project = models.ForeignKey(project, on_delete = models.CASCADE)

class dependency(models.Model):
    name = models.CharField(max_length=50)
    due = models.DateField()
    description = models.TextField()
    budget = models.FloatField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class employee_projects(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

class employee_decisions(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    decision = models.ForeignKey(decision, on_delete=models.CASCADE)
    description = models.TextField()

class issue_tags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    issue = models.ForeignKey(issue, on_delete=models.CASCADE)

class action_tags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    action = models.ForeignKey(action, on_delete=models.CASCADE)

class decision_tags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    decision = models.ForeignKey(decision, on_delete=models.CASCADE)

class assumption_tags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    assumption = models.ForeignKey(assumption, on_delete=models.CASCADE)

class risk_tags(models.Model):
    tag = models.ForeignKey(tag, on_delete=models.CASCADE)
    risk = models.ForeignKey(risk, on_delete=models.CASCADE)

