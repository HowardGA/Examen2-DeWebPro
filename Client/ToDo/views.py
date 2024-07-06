from django.shortcuts import render, redirect
from django.views import generic
import requests
#from .forms import CreateGrantGoalClientForm
# Create your views here.
class ListTasksClient(generic.View):
    template_name = "ToDo/list_todo_cl.html"
    url = "http://localhost:8000/api/tasks"
    response = None
    context = {}
    
    def get(self, request):
        self.response = requests.get(url = self.url)
        self.context = {
            "todo": self.response.json()
        }
        return render(request, self.template_name, self.context)