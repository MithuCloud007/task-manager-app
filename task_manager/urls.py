
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from tasks import urls as task_urls
from rest_framework.routers import DefaultRouter
from tasks.api.views import TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(task_urls, namespace='tasks')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)