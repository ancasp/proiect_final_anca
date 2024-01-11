from django import forms
from django.db.models import TextField
from django.forms import TextInput, EmailInput, Select, DateInput, Textarea

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'trainer': Select(attrs={'class': 'form-select'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your message'}),
            'created_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'updated_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }