from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task, ActivityLog

@receiver(post_save, sender=Task)
def log_task_creation(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(action=f'Task created: {instance.title}')

@receiver(post_delete, sender=Task)
def log_task_deletion(sender, instance, **kwargs):
    ActivityLog.objects.create(action=f'Task deleted: {instance.title}')
