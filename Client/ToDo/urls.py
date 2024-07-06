from django.urls import path
from ToDo import views

app_name = "td"

urlpatterns = [
    path("client/list/task/", views.ListTasksClient.as_view(), name = "client_list_td"),
    path('client/create/task', views.CreateTasksClient.as_view(), name = "client_create_td"),
    path('client/detail/task/<int:pk>/', views.DetailTaskClient.as_view(), name = "client_detail_td"),
    path('client/update/task/<int:pk>/', views.UpdateTasksClient.as_view(), name="client_update_td"),
    path('client/delete/task/<int:pk>/', views.DeleteTasksClient.as_view(), name="client_delete_td"),
  
  #Areas
    path('client/areas/', views.ListAreasClient.as_view(), name='areas-list'),
    path('client/areas/create/', views.CreateAreaClient.as_view(), name='areas-create'),
    path('client/areas/<int:pk>/', views.DetailAreaClient.as_view(), name='areas-detail'),
    path('client/areas/<int:pk>/update/', views.UpdateAreaClient.as_view(), name='areas-update'),
    path('client/areas/<int:pk>/delete/', views.DeleteAreaClient.as_view(), name='areas-delete'),
]
