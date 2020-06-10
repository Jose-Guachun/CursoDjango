"""vistas de posts"""
#Django librerias
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
#FORMS
from posts.forms import PostForm


#models
from posts.models import Post

class PostFeedView(LoginRequiredMixin, ListView):
    #retornar todas las publicaciones
    template_name='posts/feed.html'
    model=Post
    ordering=('-created',)
    paginate_by=20
    context_object_name='posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    #retornar detalle de post
    template_name='posts/detail.html'
    queryset=Post.objects.all()
    context_object_name='post'


class CreatedPostView(LoginRequiredMixin, CreateView):
    #Crear un nuevo post
    template_name='posts/new.html'
    form_class=PostForm
    success_url=reverse_lazy('posts:feed')


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context


