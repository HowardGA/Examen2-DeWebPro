from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings


class Area(models.Model):
    area_name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.area_name

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username


CHOICES_LEVEL = (
    ("HIGH", "High"),
    ("MEDIUM", "Medium"),
    ("LOW", "Low"),
)

CHOICES_STATE = (
    ("PENDING", "Pending"),
    ("IN PROGRESS", "In Progress"),
    ("DONE", "Done"),
)

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=8, choices=CHOICES_LEVEL)
    state = models.CharField(max_length=16, choices=CHOICES_STATE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'


