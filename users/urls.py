#Users Urls

#Django
from django.urls import path


#importaciones de apps
from users import views

urlpatterns=[
    

    #managment
    path(
        route='login/',
        view=views.login_view,
        name='login'
        ),
    path(
        route='logout/',
        view= views.logout_view, 
        name='logout'
        ),
    path(
        route='signup/',
        view=views.signup,
        name='signup' 
         ),
    path(
        route='me/profile',
        view=views.update_profile,
        name='update'
        ),


    #posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]