from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="login"),
    path('home', views.home, name="home"),
    path('landing-page', views.login, name="landing-page"),
    path('create-account', views.create_account, name="create_account"),
    path('sign-in', views.sign_in, name="sign_in"),
    path('projects', views.projects, name="projects"),
    path('sign-out', views.sign_out, name="sign_out"),
    path('create-project', views.create_project, name="create_project"),
    path('projects/<int:pk>/', views.view_project, name="view_project"),
    path('projects/<int:pk>/add-risk', views.add_risk, name="add_risk"),
    path('projects/<int:project_pk>/risks', views.risks, name="risks"),
    path('projects/<int:project_pk>/risks/<int:risk_pk>', views.view_risk, name="view_risk"),
    path('projects/<int:pk>/add-action', views.add_action, name="add_action"),
    path('projects/<int:project_pk>/actions', views.actions, name="actions"),
    path('projects/<int:project_pk>/actions/<int:action_pk>', views.view_action, name="view_action"),
    path('projects/<int:pk>/add-assumption', views.add_assumption, name="add_assumption"),
    path('projects/<int:project_pk>/assumptions', views.assumptions, name="assumptions"),
    path('projects/<int:project_pk>/assumptions/<int:assumption_pk>', views.view_assumption, name="view_assumption"),
    path('projects/<int:pk>/add-issue', views.add_issue, name="add_issue"),
    path('projects/<int:project_pk>/issues', views.issues, name="issues"),
    path('projects/<int:project_pk>/issues/<int:issue_pk>', views.view_issue, name="view_issue"),
    path('projects/<int:pk>/add-decision', views.add_decision, name="add_decision"),
    path('projects/<int:project_pk>/decisions', views.decisions, name="decisions"),
    path('projects/<int:project_pk>/decisions/<int:decision_pk>', views.view_decision, name="view_decision"),
    path('projects/<int:pk>/add-dependency', views.add_dependency, name="add_dependency"),
    path('projects/<int:project_pk>/dependencies', views.dependencies, name="dependencies"),
    path('projects/<int:project_pk>/dependencies/<int:dependency_pk>', views.view_dependency, name="view_dependency"),

    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),

    

]