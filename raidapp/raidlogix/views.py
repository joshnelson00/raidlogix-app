from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "templates/h_and_f.html")