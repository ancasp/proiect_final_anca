from django.urls import path

# from . import views
from .views import HomeTemplateView

urlpatterns = [
    # path("salut/", salut, name = "Salut"),
    path('home/', HomeTemplateView.as_view(), name='home_page')
]