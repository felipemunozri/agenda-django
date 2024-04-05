from django.forms import DateInput, ModelForm, TextInput
from .models import Task

class TaskForm(ModelForm):

    class Meta:
        
        model = Task
        # fields = '__all__'
        exclude = ('creation_date',)
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'estimated_end': 'Fecha término (estimada)',
            'priority': 'Prioridad',
        }
        widgets = {
            'estimated_end': DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'priority': TextInput(attrs={'type': 'number', 'min': 1, 'max': 5}),
        }