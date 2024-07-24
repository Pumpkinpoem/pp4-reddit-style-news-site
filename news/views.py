from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ChangeUsernameForm, ChangeEmailForm, DeleteAccountForm, PostForm, CommentForm
from .models import Post, Comment, Category
from django.db.models import Count



#Post

def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    sort_by = request.GET.get('sort_by', 'time')

    if category_id:
        posts = Post.objects.filter(category_id=category_id)
    else:
        posts = Post.objects.all()

    if sort_by == 'popularity':
        posts = posts.annotate(num_comments=Count('comment')).order_by('-num_comments', '-created_at')
    elif sort_by == 'category':
        posts = posts.order_by('category', '-created_at')
    else:
        posts = posts.order_by('-created_at')

    return render(request, 'news/index.html', {'posts': posts, 'categories': categories})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'news/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_form.html', {'form': form, 'post': post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'news/delete_post.html', {'post': post})

@login_required
def delete_post_image(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.image = None
        post.save()
        return redirect('edit_post', slug=post.slug)
    return render(request, 'news/delete_post_image.html', {'post': post})


# post detail slug, comment, up/down vote

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'news/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'news/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        return redirect('post_detail', slug=post_slug)
    return render(request, 'news/delete_comment.html', {'comment': comment})

@login_required
def upvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)
    if request.user not in post.upvotes.all():
        post.upvotes.add(request.user)
    else:
        post.upvotes.remove(request.user)
    return redirect('post_detail', slug=slug)

@login_required
def downvote_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)
    if request.user not in post.downvotes.all():
        post.downvotes.add(request.user)
    else:
        post.downvotes.remove(request.user)
    return redirect('post_detail', slug=slug)

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
