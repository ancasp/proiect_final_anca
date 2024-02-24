from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from asbook.customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your number'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description',
                                           'rows': '3'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            # 'trainer': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data['email']
        check_emails = Customer.objects.filter(email=get_email)
        if check_emails:
            msg = 'Exista un client cu aceasta adresa de email'
            self._errors['email'] = self.error_class([msg])

        return cleaned_data
