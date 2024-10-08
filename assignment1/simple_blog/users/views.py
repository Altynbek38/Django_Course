from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Follow
from .forms import ProfileForm, UserRegisterForm, LoginForm

# Create your views here.
def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)
            return redirect('login')

    context = {
        "register_form": form,
        }    

    template = loader.get_template('registration.html')

    return HttpResponse(template.render(context, request))

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('profile_view', user.id)

    context = {
        "login_form": form,
    }

    template = loader.get_template('login.html')

    return HttpResponse(template.render(context, request))

def logout(request):
    auth.logout(request)

    return redirect("register")

@login_required(login_url='login')
def profile_view(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)

    follower_cnt = Follow.objects.filter(following=user).count()
    following_cnt = Follow.objects.filter(follower=user).count()
    is_following = Follow.objects.filter(follower=request.user, following=user).exists()

    context = {
        'profile': profile,
        'follower_cnt': follower_cnt,
        'following_cnt': following_cnt,
        "is_following": is_following,
    }

    template = loader.get_template('profile.html')

    return HttpResponse(template.render(context,request=request))

@login_required(login_url='login')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile_view', id)
    
    context = {
        "form": form,
    }
    template = loader.get_template('profile_edit.html')

    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def follow_user(request, id):
    user = get_object_or_404(User, id=id)

    follow = Follow.objects.filter(follower = request.user, following = user)
    if not follow.exists():
        Follow.objects.create(follower = request.user, following = user)

    return redirect('profile_view', id)

@login_required(login_url='login')
def unfollow_user(request, id):
    user = get_object_or_404(User, id=id)

    follow = Follow.objects.filter(follower = request.user, following = user)
    if follow.exists():
        follow.delete()

    return redirect('profile_view', id)
        
