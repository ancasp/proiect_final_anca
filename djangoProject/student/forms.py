from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
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
            'trainer': Select(attrs={'class': 'form-select'}),
        }

    # def clean() este folosita pentru a genera validari in cadrul formularului
    def clean(self):
        cleaned_data = self.cleaned_data # se stocheaza in variabiala cleaned_data un dictionar cu toate valorile introduse in formualr

        # O validare pentru unicitate pe adresa de email
        get_email = cleaned_data['email'] #avem stocat valoarea din campul email
        # Varianta 1
        check_emails = Student.objects.filter(email=get_email)
        if check_emails:
            msg = 'Exista un student cu aceasta adresa de email'
            self._errors['email'] = self.error_class([msg])


        # Varianta 2
        #all_students = Student.objects.all()
        #for student in all_students:
        #    if student.email == get_email:
        #        print('exista')

        # O unicitate pe first_name SI last_name. Nu trebuie sa salvam un student cu acelasi first_name, respectiv last_name

        get_fn = cleaned_data['first_name']
        get_ln = cleaned_data['last_name']
        check_fn_ln = Student.objects.filter(first_name=get_fn, last_name=get_ln)
        if check_fn_ln:
            msg = 'Exista un student cu acest nume si prenume'
            self._errors['first_name'] = self.error_class([msg])


        # O validare pe campul description. sa adauge cel putin 10 caractere.
        get_description = cleaned_data['description']
        if len(get_description) < 10:
            msg = 'Textul trebuie sa contina minim 10 caractere'
            self._errors['description'] = self.error_class([msg])


        # o validare pentru campurile start_date si end_date. Daca start_date > end_date sa ii afiseze o eroare
        get_start_date = cleaned_data['start_date']
        get_end_date = cleaned_data['end_date']
        if get_start_date > get_end_date:
            msg = 'Data de final nu poate fi mai mica decat data de inceput'
            self._errors['start_date'] = self.error_class([msg])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
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
            'trainer': Select(attrs={'class': 'form-select'}),
        }
