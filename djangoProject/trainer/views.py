from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer, HistoryTrainer


class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home_page')
    permission_required = 'trainer.add_trainer'

    def form_valid(self, form):
        if form.is_valid():
            new_trainer = form.save()

            get_message = f'Trainerul cu numele {new_trainer.first_name} {new_trainer.last_name} a fost inregistrat'

            HistoryTrainer.objects.create(
                message=get_message,
                created_at=datetime.datetime.now(),
                active=True,
                user_id=self.request.user.id
            )

        return redirect('list-of-trainers')


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_list_of_trainers'


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.change_trainer'


class TrainerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.delete_trainer'

class TrainerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'trainer/detail_trainer.html'
    model = Trainer
    permission_required = 'trainer.view_trainer'

class HistoryTrianerListView(LoginRequiredMixin, ListView):
    template_name = ''
    model = HistoryTrainer
    context_object_name = ''