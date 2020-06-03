"""vistas de posts"""
#Django librerias
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
#FORMS
from posts.forms import PostForm


#models
from posts.models import Post

class PostFeedView(LoginRequiredMixin, ListView):
    template_name='posts/feed.html'
    model=Post
    ordering=('-created',)
    paginate_by=5
    context_object_name='posts'


@login_required
def create_post(request):
    #crear un nuevo post
    if  request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form=PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user': request.user,
            'profile': request.user.profile
        }
    )

