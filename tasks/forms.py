from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'creation_date_time': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.TextInput(attrs={'class': 'form-control'}),
            'priority':  forms.Select(attrs={'class': 'form-control'}),
            'completed': forms.TextInput(attrs={'class': 'form-control'}),
            'photos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            
        }
class TaskSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))