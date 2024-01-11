from django.urls import path

from intro import views

urlpatterns = [
    path('first-page/', views.first_page, name='first-page'),
    path('second-page/', views.second_page, name='second-page'),
    path('list_cars/', views.cars, name='list-cars'),
    path('list_books/', views.books, name='list-books'),
]

# Prefixul ESTE UNIC
# Name-ul ESTE UNIC

# NU DEFINITI 2 path() la fel!
# Fiecare path va apela functia/clasa.
