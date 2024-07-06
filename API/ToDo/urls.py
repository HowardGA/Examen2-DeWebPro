from django.urls import path
from ToDo import views

app_name = 'api'

urlpatterns = [
    # Task 
    path('tasks/', views.ListTaskAPIView.as_view(), name='task-list'),
    path('tasks/create/', views.CreateTaskAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.DetailTaskAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', views.UpdateTaskAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.DeleteTaskAPIView.as_view(), name='task-delete'),
    
    # Task with with filters
    path('tasks/ids/', views.ListTaskIDOnlyAPIView.as_view(), name='task-ids'),
    path('tasks/id-titles/', views.ListTaskIDTitleAPIView.as_view(), name='task-id-titles'),
    path('tasks/unresolved/', views.UnresolvedTasksAPIView.as_view(), name='task-unresolved'),
    path('tasks/resolved/', views.ResolvedTasksAPIView.as_view(), name='task-resolved'),
    path('tasks/userids/', views.ListTaskUserIDAPIView.as_view(), name='task-userids'),
    path('tasks/resolved/userids/', views.ResolvedTasksUserIDAPIView.as_view(), name='task-resolved-userids'),
    path('tasks/unresolved/userids/', views.UnresolvedTasksUserIDAPIView.as_view(), name='task-unresolved-userids'),

    # Area 
    path('areas/', views.ListAreaAPIView.as_view(), name='areas-list'),
    path('areas/create/', views.CreateAreaAPIView.as_view(), name='areas-create'),
    path('areas/<int:pk>/', views.DetailAreaAPIView.as_view(), name='areas-detail'),
    path('areas/<int:pk>/update/', views.UpdateAreaAPIView.as_view(), name='areas-update'),
    path('areas/<int:pk>/delete/', views.DeleteAreaAPIView.as_view(), name='areas-delete'),
    
    # Comment 
    path('comments/create/', views.CreateCommentAPIView.as_view(), name='comments-create'),
    path('comments/<int:pk>/', views.DetailCommentAPIView.as_view(), name='comments-detail'),
    path('comments/<int:pk>/delete/', views.DeleteCommentAPIView.as_view(), name='comments-delete'),
    
    #User
     path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),

]
