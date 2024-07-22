from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ChangeUsernameForm, ChangeEmailForm, DeleteAccountForm
from .models import Post
from .forms import PostForm
from django.db.models import Count


#Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'news/index.html', {'posts': posts})
    sort_by = request.GET.get('sort_by', 'time')

    if sort_by == 'popularity':
        posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments', '-created_at')
    elif sort_by == 'category':
        posts = Post.objects.order_by('category', '-created_at')
    else:
        posts = Post.objects.order_by('-created_at')

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


# post detail slug

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'news/post_detail.html', {'post': post})

# account profile

@login_required
def account_profile(request):
    return render(request, 'news/account_profile.html')

# user account settings

@login_required
def account_settings(request):
    return render(request, 'news/account_settings.html')

#user account functions

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