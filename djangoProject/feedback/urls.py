
from django.urls import path
from feedback import views

urlpatterns = [
     path('create_feedback/', views.FeedbackCreateView.as_view(), name='create-feedback')

]