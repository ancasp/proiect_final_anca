from django.contrib import admin

from student.models import Student, HistoryStudent
from trainer.models import Trainer

# Register your models here.
admin.site.register(Student)
admin.site.register(Trainer)
