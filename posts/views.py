"""vistas de posts"""
#Django librerias
from django.shortcuts import render

#utilidades
from datetime import datetime


posts=[
    {
        'name':'Logo Drekx',
        'user':'Jose',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture': "https://i.imgur.com/XXzwgDKl.png",

    },
    {
        'name':'D Franco',
        'user':'Ginger',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture': "https://i.imgur.com/hIaGPg0.jpg",

    },
    {
        'name':'Colinas',
        'user':'John',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'picture': "https://imgur.com/LLKjaSj.jpg",

    },
]

def list_posts(request):
    return render(request, 'field.html', {'posts':posts})

