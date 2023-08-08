from msilib.schema import ListView
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'index.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)