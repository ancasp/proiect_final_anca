from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
@login_required()
def first_page(request):
    return HttpResponse('Hello world!')

@login_required()
def second_page(request):
    return HttpResponse('Hello Anca!')

@login_required()
def cars(request):
    context = {
        'all_cars': [
            {
                'brand': 'Mercedes',
                'color': 'black',
                'year': 2023
            },
            {
                'brand': 'Mini Cooper',
                'color': 'red',
                'year': 2022
            },
            {
                'brand': 'Ford',
                'color': 'white',
                'year': 2020
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', context)

@login_required()
def books(request):
    context = {
        'all_books': [
            {
                'titlu': 'Ion',
                'autor': 'Liviu Rebreanu',
                'editura': 'Litera'
            },

             {
                'titlu': 'Baltagul',
                'autor': 'Mihail Sadoveanu',
                'editura': 'Humanitas'
            },

            {
                'titlu': 'Morometii',
                'autor': 'Marin Preda',
                'editura': 'Univers'
            }
        ]
    }

    return render(request, 'intro/list_of_books.html', context)