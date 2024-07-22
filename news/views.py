from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ChangeUsernameForm, ChangeEmailForm, DeleteAccountForm
from .models import Post
from .forms import PostForm

#Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'news/index.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'news/create_post.html', {'form': form})

# user account

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('account_profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})

@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            request.user.username = form.cleaned_data['username']
            request.user.save()
            return redirect('account_profile')
    else:
        form = ChangeUsernameForm(initial={'username': request.user.username})
    return render(request, 'account/change_username.html', {'form': form})

@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('account_profile')
    else:
        form = ChangeEmailForm(initial={'email': request.user.email})
    return render(request, 'account/change_email.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            request.user.delete()
            return redirect('account_logout')
    else:
        form = DeleteAccountForm()
    return render(request, 'account/delete_account.html', {'form': form})