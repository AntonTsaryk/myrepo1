from django.urls import path
from .views import PostView, PostCreateView


urlpatterns = [
    path('home/', PostView.as_view(), name='home'),
    path('new_post/', PostCreateView.as_view(), name='new_post')
]




