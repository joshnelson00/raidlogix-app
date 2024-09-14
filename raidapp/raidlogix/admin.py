from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(project)
admin.site.register(tag)
admin.site.register(issue)
admin.site.register(action)
admin.site.register(decision)
admin.site.register(assumption)
admin.site.register(risk)
admin.site.register(dependency)
admin.site.register(user_decisions)
admin.site.register(user_projects)
admin.site.register(risk_tags)
admin.site.register(action_tags)
admin.site.register(issue_tags)
admin.site.register(decision_tags)
admin.site.register(assumption_tags)

