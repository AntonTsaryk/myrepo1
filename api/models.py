from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', null=True, blank=True)
    USER_TYPE_CHOICES = (
        ('CLIENT', 'Client'),
        ('CRAFTSMAN', 'Craftsman'),
    )
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default='CLIENT')
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='craftsman')
    description = models.TextField()
    specializations = models.ManyToManyField(ServiceCategory)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='comments_on_worker')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.worker}"


class Job(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posted_jobs')
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name='jobs')
    date_posted = models.DateField()
    location = models.CharField(max_length=50)
    price_estimation = models.PositiveIntegerField(
        help_text="Estimated price for the job")
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='OPEN')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class JobOffer(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,
                            related_name='offers_to_craftsmen')
    craftsman = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='job_offers_received')
    date_offered = models.DateField()

    def __str__(self):
        return f"{self.job.client} offered {self.job.title} to {self.craftsman.user.username}"
