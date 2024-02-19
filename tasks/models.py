from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date_time = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    completed = models.BooleanField(default=False)
    photos = models.ManyToManyField('Photo', blank=True, related_name='task_photo')

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.FileField(upload_to='tasks/photos/')
    
    def __str__(self):
        return str(self.image)

   