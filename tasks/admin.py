from django.contrib import admin
from tasks.models import Task,Photo

# Register your models here.
admin.site.register(Task)
admin.site.register(Photo)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','creation_date_time','due_date','priority','completed','photos')
    search_fields = ('title')
    list_filter = ('creation_date_time','due_date','priority','completed')