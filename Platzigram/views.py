#views platzigram

#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json


def hello_world(request):
    now=datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    return HttpResponse('La fecha y hora del servidor es: {now}'.format(now=str(now)))


def sorted_required(request):
    numbers =[int(i)
    for i in request.GET['numbers'].split(',')]
    sorted_ints=sorted(numbers)
    data={
        'satatus':'ok',
        'numbers':sorted_ints,
        'message': 'Integracion de sorted correcto'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type="aplication/json")


def  say_hi(request, name, age):   
    if age<12:
        message='Lo sentimos {}, tu eres menor de edad'.format(name)
    else:
        message='hola, {}! Bienvenido a dreks'.format(name)
    return HttpResponse(message)