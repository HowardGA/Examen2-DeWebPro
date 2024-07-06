from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ToDo.models import Task, Tag, Area, Comment, Attachment, ActivityLog
from ToDo.serializers import (
     DetailTaskSerializer, TagSerializer, AreaSerializer,
    CommentSerializer, AttachmentSerializer, ActivityLogSerializer
)


# Task 
class ListTaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer

class DetailTaskAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer

class CreateTaskAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer

class UpdateTaskAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer

class DeleteTaskAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer


# Tag 
class ListTagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DetailTagAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CreateTagAPIView(generics.CreateAPIView):
    serializer_class = TagSerializer

class UpdateTagAPIView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DeleteTagAPIView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Area 
class ListAreaAPIView(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class DetailAreaAPIView(generics.RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class CreateAreaAPIView(generics.CreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class UpdateAreaAPIView(generics.UpdateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class DeleteAreaAPIView(generics.DestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

# Comment 

class DetailCommentAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CreateCommentAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    
class DeleteCommentAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Attachment


# ActivityLog 
class ListActivityLogAPIView(generics.ListAPIView):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

class DetailActivityLogAPIView(generics.RetrieveAPIView):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    
@receiver(post_save, sender=Task)
def log_task_creation(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(action=f'Task created: {instance.title}')

@receiver(post_delete, sender=Task)
def log_task_deletion(sender, instance, **kwargs):
    ActivityLog.objects.create(action=f'Task deleted: {instance.title}')
    
