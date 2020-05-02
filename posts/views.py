"""vistas de posts"""
#Django librerias
from django.http import HttpResponse
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
    content=[]
    for post in posts:
        content.append(""" 
        <p><strong>{name}</strong></p>
        <p><small>{user}- <i>{timestamp}</i></small></p> 
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))

