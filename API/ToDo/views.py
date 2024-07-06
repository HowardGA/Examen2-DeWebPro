from rest_framework import generics
from ToDo.models import Task, Area, Comment, CustomUser
from ToDo.serializers import (
    DetailTaskSerializer, CreateTaskSerializer,
    AreaSerializer, CommentSerializer, UserSerializer,
    TaskIDSerializer, TaskIDTitleSerializer,
    UnresolvedTasksSerializer, ResolvedTasksSerializer,
    TaskUserIDSerializer, ResolvedTasksUserIDSerializer,
    UnresolvedTasksUserIDSerializer
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
    serializer_class = CreateTaskSerializer

class UpdateTaskAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer

class DeleteTaskAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = DetailTaskSerializer
    
# Asked serializers:
class ListTaskIDOnlyAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskIDSerializer  #only task ID
    
class ListTaskIDTitleAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskIDTitleSerializer  # Every task, only ID and title

class UnresolvedTasksAPIView(generics.ListAPIView):
    serializer_class = UnresolvedTasksSerializer  # Every pending task, only ID and titkes

    def get_queryset(self):
        return Task.objects.filter(state='PENDING')

class ResolvedTasksAPIView(generics.ListAPIView):
    serializer_class = ResolvedTasksSerializer  # Every resolverd task, ID and titles

    def get_queryset(self):
        return Task.objects.filter(state='DONE')

class ListTaskUserIDAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUserIDSerializer  # Every task by id and user

class ResolvedTasksUserIDAPIView(generics.ListAPIView):
    serializer_class = ResolvedTasksUserIDSerializer  # every resolverd task by ID and User

    def get_queryset(self):
        return Task.objects.filter(state='DONE')

class UnresolvedTasksUserIDAPIView(generics.ListAPIView):
    serializer_class = UnresolvedTasksUserIDSerializer  # Every pending task user n ID

    def get_queryset(self):
        return Task.objects.filter(state='PENDING')

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

# User    
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer