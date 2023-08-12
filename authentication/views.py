from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from api.models import Job
from django.views.generic import ListView


    
class JobView(ListView):
    #make several models
    model = Job
    template_name = 'index.html'
    context_object_name = 'object_list' 
    
class HomeView(TemplateView):
    template_name = 'home.html'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'home.html', {'error': 'Bad credentials'})
    else:
        return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

