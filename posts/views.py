from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form .is_valid():

            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(
                form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:

            return HttpResponseRedirect(form.erros.as_json())
    return render(request, "edit.html", {"post": post})

def like(request, post_id):
    newlikecount = Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')