from django.urls import path
from . import views
from .views import JobView


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('available-jobs/', JobView.as_view(), name='availablejobs'),
    
]


