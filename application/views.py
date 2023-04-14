from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def projects(request):
    return render(request,'projects.html')
def whatwedo(request):
    return render(request,'whatwedo.html')
def blogs(request):
    return render(request,'blogs.html')
def contacts(request):
    return render(request,'contacts.html')








