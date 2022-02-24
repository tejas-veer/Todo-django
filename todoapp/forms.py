from django.forms import ModelForm,widgets
from .models import TodoList
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['taskText']
        widgets = {
            'taskText' : forms.TextInput(attrs={'class':'todo-input' , 'placeholder':'Enter Task and Press Enter '})
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['taskText'].label = ""
