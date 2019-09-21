from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.models import project
from posts.forms import createProject


# Create your views here.
def project_page(request):
    """ Create a view that will return a list
    of posts that are published prior to now
    and render them to the blogpost.html template
    """
    projects = project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"posts.html", {'projects': projects})


@login_required
def project_create(request):
    """project form"""

    if request.method == "POST":
        newProject_form = createProject(request.POST)

        if newProject_form.is_valid():
            '''dont commit the form and add user before saving the form
            otherwise gives problems'''
            instance = newProject_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(project_page)

    else:
        newProject_form = createProject()
    return render(request, 'create_posts.html', {'newProject_form': newProject_form})

def edit_project(request, pk=None):
    """create a view that allows us to create
    or edit a post depending if the post ID
    is null or not
    """

    post = get_object_or_404(project, pk=pk) if pk else None
    if request.method=='POST':
        form = createProject(request.POST, request.FILES, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(project_page)
    else:
        form = createProject(instance=post)
    return render(request, 'posts_form.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(project, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect(project_page)
    return render(request,"posts.html")
