
from django.urls import path

from asbook.customer import views

urlpatterns = [
    path('', views.CustomerCreateView.as_view(), name='create-customer'),
    # path('list_of_customers/', views.CustomerListView.as_view(), name='list-of-customers'),
    # path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    # path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    # path('details_student/<int:pk>/', views.StudentDetailView.as_view(), name='details-student'),
    # path('history/', views.HistoryCustomerListView.as_view(), name='history'),
    ]