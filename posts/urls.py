#post Urls

#Django
from django.urls import path

#views
from posts import views

urlpatterns=[
    path(
        route='',
        view=views.PostFeedView.as_view(), 
        name='feed'
        ),


    path(
        route='posts/new/',
        view=views.CreatedPostView.as_view(), 
        name='create'
        ),


    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
        ),
    
    
]

    
    