from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from posts.models import project


def index(request):
    """Return the index.html file"""
    return render(request,'index.html')

''' this is a test for templates layout '''
def testpage(request):
    """Return the index.html file"""
    return render(request,'tests/test.html')

def about(request):
    """Return the index.html file"""
    return render(request,'about.html')

def contact(request):
    """Return the index.html file"""
    return render(request,'contact.html')

def services(request):
    """Return the index.html file"""
    return render(request,'services.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            # profile = profile_form.save(commit=False)
            # profile.author = request.user
            # profile.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
            return redirect(reverse('index'))
    else:
        registration_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form,"profile_form": profile_form})


def user_profile(request):
    """The user's profile page"""
    userMail = User.objects.get(email=request.user.email)
    myProjects = project.objects.all().order_by('published_date')
    return render(request, 'profile.html', {"profile": userMail, "myProjects": myProjects})

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
