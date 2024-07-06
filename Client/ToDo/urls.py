from django.urls import path
from ToDo import views

app_name = "td"

urlpatterns = [
    path("client/list/task/", views.ListTasksClient.as_view(), name = "client_list_td"),
  


]
