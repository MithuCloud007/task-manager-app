from django.urls import path
from .views import TaskListView,TaskAdd,TaskUpdate,TaskView,TaskDelete

app_name='tasks'

urlpatterns = [
    path('add-task', TaskAdd.as_view(), name="add_task"),
    path('', TaskListView.as_view(), name="all_tasks"),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name="update_task"),
    path('view-task/<int:pk>', TaskView.as_view(), name="view_task"),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name="delete_task"),

]