from django.shortcuts import render, redirect
from django.views import generic
import requests
from .forms import CreateTaskForm, AreaForm
# Create your views here.
class ListTasksClient(generic.View):
    template_name = "ToDo/list_todo_cl.html"
    base_url = "http://localhost:8000/api/tasks/"
    response = None
    context = {}
    
    def get(self, request):
        filter_params = {}
        selected_endpoint = request.GET.get('endpoint')
        url = self.base_url
        
        # Determine which endpoint to use based on selected option
        if selected_endpoint == 'ids':
            url += 'ids/'
        elif selected_endpoint == 'id-titles':
            url += 'id-titles/'
        elif selected_endpoint == 'unresolved':
            url += 'unresolved/'
        elif selected_endpoint == 'resolved':
            url += 'resolved/'
        elif selected_endpoint == 'userids':
            url += 'userids/'
        elif selected_endpoint == 'resolved-userids':
            url += 'resolved/userids/'
        elif selected_endpoint == 'unresolved-userids':
            url += 'unresolved/userids/'
        else:
            # Default to all tasks
            pass
        
        self.response = requests.get(url=url)
        self.context = {
            "todo": self.response.json()
        }
        return render(request, self.template_name, self.context)

class CreateTasksClient(generic.CreateView):
    template_name = "ToDo/create_todo_cl.html"
    url = "http://localhost:8000/api/tasks/create/"
    users_url = "http://localhost:8000/api/users/"
    areas_url = "http://localhost:8000/api/areas/"
    context = {}
    form_class = CreateTaskForm
    
    def get(self, request):
        users_response = requests.get(self.users_url)
        areas_response = requests.get(self.areas_url)
        
        users = [(user['id'], f"{user['first_name']} {user['last_name']}") for user in users_response.json()]
        areas = [(area['id'], area['area_name']) for area in areas_response.json()]
        
        form = self.form_class()
        form.fields['user'].choices = users
        form.fields['area'].choices = areas
        
        self.context = {
            "form": form
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        payload = {
            "title": request.POST['title'],
            "description": request.POST['description'],
            "due_date": request.POST['due_date'],
            "priority": request.POST['priority'],
            "state": request.POST['state'],
            "user": request.POST['user'],
            "area": request.POST['area']
        }
        response = requests.post(url=self.url, json=payload)  
        print(payload);
        return redirect("td:client_list_td")
    
class DetailTaskClient(generic.View):
    template_name = "ToDo/detail_todo_cl.html"
    context = {}
    url = "http://localhost:8000/api/tasks/"
    response = None
    
    def get(self, request, pk):
        self.url = self.url + f'{pk}'
        self.response = requests.get(url = self.url)
        self.context = {
            "todo": self.response.json()
        }
        return render(request, self.template_name, self.context)

class UpdateTasksClient(generic.View):
    template_name = "ToDo/update_todo_cl.html"
    url = "http://localhost:8000/api/tasks/"
    users_url = "http://localhost:8000/api/users/"
    areas_url = "http://localhost:8000/api/areas/"
    context = {}
    form_class = CreateTaskForm
    
    def get(self, request, pk):
        task_response = requests.get(self.url + f'{pk}/')
        task_data = task_response.json()
        
        users_response = requests.get(self.users_url)
        areas_response = requests.get(self.areas_url)
        
        users = [(user['id'], f"{user['first_name']} {user['last_name']}") for user in users_response.json()]
        areas = [(area['id'], area['area_name']) for area in areas_response.json()]
        
        form = self.form_class(initial=task_data)
        form.fields['user'].choices = users
        form.fields['area'].choices = areas
        
        self.context = {
            "form": form,
            "task_id": pk
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request, pk):
        payload = {
            "title": request.POST['title'],
            "description": request.POST['description'],
            "due_date": request.POST['due_date'],
            "priority": request.POST['priority'],
            "state": request.POST['state'],
            "user": request.POST['user'],
            "area": request.POST['area']
        }
        response = requests.put(url=self.url + f'{pk}/update/', json=payload)  
        return redirect("td:client_list_td")

class DeleteTasksClient(generic.View):
    template_name = "ToDo/delete_todo_cl.html"
    url = "http://localhost:8000/api/tasks/"

    def get(self, request, pk):
        task_response = requests.get(f"{self.url}{pk}/")
        task_data = task_response.json()

        context = {
            "task": task_data
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        try:
            response = requests.delete(f"{self.url}{pk}/delete/")
            response.raise_for_status()  # Raise an exception for HTTP errors

            return redirect("td:client_list_td")
        except requests.exceptions.RequestException as e:
            # Handle exceptions, log, or render an error page
            print(f"Error deleting task: {e}")
            return render(request, self.template_name, {"error": "Failed to delete task."})
        
#AREAS

class ListAreasClient(generic.View):
    template_name = "ToDo/list_areas_cl.html"
    url = "http://localhost:8000/api/areas/"
    response = None
    context = {}
    
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "areas": self.response.json()
        }
        return render(request, self.template_name, self.context)

class CreateAreaClient(generic.View):
    template_name = "ToDo/create_area_cl.html"
    url = "http://localhost:8000/api/areas/create/"
    context = {}
    form_class = AreaForm
    
    def get(self, request):
        form = self.form_class()
        self.context = {"form": form}
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            payload = form.cleaned_data
            response = requests.post(url=self.url, json=payload)
            return redirect("td:areas-list")
        else:
            self.context = {"form": form}
            return render(request, self.template_name, self.context)

class DetailAreaClient(generic.View):
    template_name = "ToDo/detail_area_cl.html"
    url = "http://localhost:8000/api/areas/"
    response = None
    
    def get(self, request, pk):
        self.url = self.url + f'{pk}/'
        self.response = requests.get(url=self.url)
        self.context = {"area": self.response.json()}
        return render(request, self.template_name, self.context)

class UpdateAreaClient(generic.View):
    template_name = "ToDo/update_area_cl.html"
    url = "http://localhost:8000/api/areas/"
    context = {}
    form_class = AreaForm
    
    def get(self, request, pk):
        area_response = requests.get(self.url + f'{pk}/')
        area_data = area_response.json()
        form = self.form_class(initial=area_data)
        self.context = {
            "form": form,
            "area_id": pk
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            payload = form.cleaned_data
            response = requests.put(url=self.url + f'{pk}/update/', json=payload)
            return redirect("td:areas-list")
        else:
            self.context = {"form": form}
            return render(request, self.template_name, self.context)

class DeleteAreaClient(generic.View):
    template_name = "ToDo/delete_area_cl.html"
    url = "http://localhost:8000/api/areas/"
    
    def get(self, request, pk):
        area_response = requests.get(f"{self.url}{pk}/")
        area_data = area_response.json()
        context = {"area": area_data}
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        response = requests.delete(f"{self.url}{pk}/delete/")
        return redirect("td:areas-list")
