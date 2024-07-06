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

    # Tag 
    path('tags/', views.ListTagAPIView.as_view(), name='tag-list'),
    path('tags/create/', views.CreateTagAPIView.as_view(), name='tag-create'),
    path('tags/<int:pk>/', views.DetailTagAPIView.as_view(), name='tag-detail'),
    path('tags/<int:pk>/update/', views.UpdateTagAPIView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.DeleteTagAPIView.as_view(), name='tag-delete'),

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
    # Attachment 

    # ActivityLog 
    path('ActivityLog/', views.ListActivityLogAPIView.as_view(), name='areas-list'),
    path('ActivityLog/<int:pk>/', views.DetailActivityLogAPIView.as_view(), name='ActivityLog-detail'),
]
