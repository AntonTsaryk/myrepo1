from django.contrib import admin

# Register your models here.
from .models import User, ServiceCategory, Worker, Job, JobOffer, Comment

admin.site.register(User)
admin.site.register(ServiceCategory)
admin.site.register(Worker)
admin.site.register(Job)
admin.site.register(JobOffer)
admin.site.register(Comment)
