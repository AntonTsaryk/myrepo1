from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storis.urls'), name='home'),
    path('authentication/', include('authentication.urls')),
]


