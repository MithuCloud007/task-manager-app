from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db import models
from .models import Task
from .forms import TaskForm
from .forms import TaskSearchForm
from django.db.models import Q

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/all.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = queryset.filter(
               Q(title__icontains=search_query) |
               Q(description__icontains=search_query) |
               Q(priority__icontains=search_query) |
               Q(creation_date_time__icontains=search_query) |
               Q(due_date__icontains=search_query) |
               Q(completed__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskSearchForm(self.request.GET)
        return context

# class TaskListView(ListView):
#     model = Task
#     context_object_name = 'tasks'
#     template_name = 'tasks/all.html'
    
class TaskAdd(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add.html'
    success_url= reverse_lazy('tasks:all_tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url= reverse_lazy('tasks:all_tasks') 
    
    
class TaskView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/view.html' 
    
class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/tasks_confirm_delete.html' 
    success_url= reverse_lazy('tasks:all_tasks')  
    


# class TaskListView(ListView):
#     model = Task
#     context_object_name = 'tasks'
#     template_name = 'tasks/all.html'
#     paginate_by = 10  # Adjust as needed

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         # Get the search parameters from the request
#         title_query = self.request.GET.get('title', '')
#         creation_date_time_query = self.request.GET.get('creation_date_time', '')
#         due_date_query = self.request.GET.get('due_date', '')
#         priority_query = self.request.GET.get('priority', '')
#         completed_query = self.request.GET.get('completed', '')

#         # Filter tasks based on search parameters
#         if title_query:
#             queryset = queryset.filter(title__icontains=title_query)

#         if creation_date_time_query:
#             queryset = queryset.filter(creation_date_time__icontains=creation_date_time_query)

#         if due_date_query:
#             queryset = queryset.filter(due_date=due_date_query)

#         if priority_query:
#             queryset = queryset.filter(priority=priority_query)

#         if completed_query:
#             queryset = queryset.filter(completed=completed_query.lower() == 'true')

#         return queryset
                       