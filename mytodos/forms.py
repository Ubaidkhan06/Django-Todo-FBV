from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Todo

class TodoForm(forms.ModelForm):
    """Form definition for Todo."""

    class Meta:
        """Meta definition for Todoform."""
        model = Todo
        fields = '__all__'
        widgets = {
            'title' : TextInput(attrs={'class':'form-control bg-danger bg-opacity-10'}),
            'description' : Textarea(attrs={'class':'form-control bg-danger bg-opacity-10'}),
        }
