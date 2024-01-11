from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateView: este o clasa dezvoltatata de Django pentru a afisa un sablon (o pagina html)

# Principalele caracteristici:

# Manipularea sabloanelor: este proiectat pentru a lucra cu pagini .html in care puteti sa specificati
# template-ul pe care doriti sa il utilizati pentru a afisa continutul

# Gestionarea contextului: puteti sa furnizati context suplimentare pentru template, permitand astfel
# trimiterea de variabile si informatii catre template pentru a fi afisare.


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'

# Implementare TemplateView:

# STEP1: Definirea in fisierul views.py din aplicatia home o noua clasa numita HomeTemplateView care a mostenit
# clasa generica TemplateView (dezvoltata de Django) si completarea template_name-ului

# STEP2: Adaugara unui folder nou numit home in folderul templates iar in acest folder, home, am creat o pagina noua
# .html numita home_page unde am adaugat continut.

# STEP3: In fisierul urls.py din aplicatia home am definit path() pentru clasa HomeTemplateView

# STEP4: In folderul templates este regasit fisierul .html navbar unde am adaugat pe tag <a> in care este trimiterea
# catre pagina .html name-ul urlui pentru home_page