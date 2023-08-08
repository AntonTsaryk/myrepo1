from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView

def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(request,username=username,password=password)
        if user is not None:    
            login(request,user)
            return redirect ('home')
        else:
            return render(request, 'authentication/home.html', {'error': 'Bad credentials'})
    else: 
        return render(request, 'authentication/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(TemplateView):
    template_name = 'home.html'
