from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent
from trainer.forms import TrainerForm


# CreateView este o clasa dezvoltata de Django care va ajuta sa va definiti un obiect in baza de date
# si afisarea unui formular asociat modelului definit in models.py

# Caracteristici:

# Formular de Creare: automat se genereaza un formular asociat modelui pentru a adauga un obiect
# Procesarea datelor: gestiona procesarea datelor introduse in formular prin validare
# Redirectionare dupa creare: in momentul in care obiectul este creat cu success, utilizatorul poate fi
# rediretionat pe pagina dorita de noi.

class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('home_page')
    permission_required = 'student.add_student'

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save()

            get_message = f'Studentul cu numele {new_student.first_name} {new_student.last_name} a fost inregistrat'

            HistoryStudent.objects.create(message=get_message,
                                          created_at=datetime.datetime.now(),
                                          active=True,
                                          user_id=self.request.user.id)

        return redirect('list-of-students')


# ListView este o clasa dezvoltata de Django care va ajuta pentru a afisarea unei liste de obiecte
# dintr-un model in template

# Principalele caracteristici:

# Gestionarea listei: automatizeaza procesul de preluare a listei de obiecte dintr-un model
# Template implicit: ListView foloseste un sablin implicit dar va lasa sa il folositi pe  al vostru.

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'  # Student.objects.all() # default
    permission_required = 'student.view_list_of_students'

    # get_queryseet este o metoda definita in clasele de view-ur( ListView) pentru a obtine setul de obiecte pe care
    # sa le afiseze sau sa le proceseze in intergata. Controla datele pe care le veti accesa in interfata
    def get_queryset(self):
       return Student.objects.filter()

# UpdateView este o clasa generica in Django utilizata pentru a afisa si actualiza datele unui obiect existent
# intr-o baza de date.

class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.change_student'


# DeleteView este o clasa generica in Django utilizate pentru a sterge un obiect dintr-o baza de date folosind
# un mecanism simplificat si standarlzat.


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.delete_student'

# DetailView este o clasa generica in Django utilizata pentru a afisa detaliile unui obiect.

class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/detail_student.html'
    model = Student
    permission_required = 'student.view_student'


class HistoryStudentListView(LoginRequiredMixin, ListView):
    template_name = 'student/history_student.html'
    model = HistoryStudent
    context_object_name = 'all_historystudents'



def get_all_students_per_trainer(request, pk):
    get_students = Student.objects.filter(trainer_id=pk) # Filtrez dupa coloana trainer_id si voi aduce toti
    #studentii alocati acelui trainer (pk)

    return render(request, 'student/list_of_students.html', {'all_students': get_students})