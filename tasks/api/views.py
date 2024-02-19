from rest_framework import viewsets
from .serializers import TaskSerializers
from tasks.models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    