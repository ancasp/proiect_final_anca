import datetime
import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import DEFAULT_FROM_EMAIL
from userextend.forms import UserForm
from userextend.models import UserHistory


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')


    # metoda form_valid este o partea a claselor bazate pe view(CREATEVIEW, UPDATVIEW, FORMVIEW), ROLUL
    # principal al metodei este de a procesa datele formularului validat. Cand un formaular este trimis, Django
    # il valideaza automat verificand daca toate campurile sunt completate corect conform definitiilor din forms.py


    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False) # datele introduse in formaular nu se salveaza in baza de date, cand am commit=False
            # in new user stochez o instant a modelui User
            new_user.first_name = new_user.first_name.title()
            # atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
            new_user.last_name = new_user.last_name.title()
            new_user.email = new_user.email.lower()

            #generare username
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "" )}_{random.randint(100000, 999999)}'

            new_user.save()

            # Trimitere mail FARA TEMPLATE
            subject = 'Cont nou in aplicatie'
            message = f'''Felicitari!
            Contul a fost adaugat cu success.
            Pentru autentificare ai nevoie de un username. Username este: {new_user.username}
            '''
            #send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])

            # Trimitere mail CU TEMPLATE

            details_user = {
                'fullname': f'{new_user.first_name.title()} {new_user.last_name.title()}',
                'user_name': new_user.username
            }

            subject = 'Adaugare cont nou'
            message = get_template('mail.html').render(details_user)
            mail = EmailMessage(
                subject, message, DEFAULT_FROM_EMAIL, [new_user.email]
            )
            mail.content_subtype = 'html'
            #mail.send()

            #Istoric
            get_message = (f'S-a inregistrat un user nou.First name:{new_user.first_name}'
                     f', last name: {new_user.last_name}, username:{new_user.username},'
                     f'email: {new_user.email}')

            UserHistory.objects.create(message=get_message,
                                       created_at=datetime.datetime.now(),
                                       updated_at=datetime.datetime.now())



        return redirect('login')

