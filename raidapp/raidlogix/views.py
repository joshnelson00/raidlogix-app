from django.shortcuts import render

# Create your views here.
def template(request):
    return render(request, "h_and_f.html")

def home(request):
    return render(request, "home.html")