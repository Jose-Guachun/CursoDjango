#platzigram modulo de URLS de platzi

from django.contrib import admin
from django.urls import path
from Platzigram import views


urlpatterns = [
    path('hello-world/', views.hello_world),
    path ('sorted/', views.sorted_required),
    path('hi/<str:name>/<int:age>/', views.say_hi)
]
