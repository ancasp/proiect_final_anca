from django.urls import path

# from . import views
from .views import HomeTemplateView

urlpatterns = [
    # path("salut/", salut, name = "Salut"),
    path('', HomeTemplateView.as_view(), name='home_page')
]
#C:\Users\ancas\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe