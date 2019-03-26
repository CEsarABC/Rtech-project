from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.models import project
from posts.forms import createProject


# Create your views here.

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
            return redirect(project_create)

    else:
        newProject_form = createProject()
    return render(request, 'posts.html', {'newProject_form': newProject_form})
    