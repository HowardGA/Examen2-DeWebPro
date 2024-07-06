from django.db import models
from django.contrib.auth.models import User
    
class Area(models.Model):
    area_name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.area_name

CHOICES_LEVEL = (
    ("HIGH", "High"),
    ("MEDIUM", "Medium"),
    ("LOW", "Low"),
)

CHOICES_STATE = (
    ("PENDING", "Pending"),
    ("IN_PROGRESS", "In Progress"),
    ("DONE", "Done"),
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Attachment for {self.task.title}'


class ActivityLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.action} by {self.user.username} on {self.task.title}'
