from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ChangeUsernameForm, ChangeEmailForm, DeleteAccountForm, PostForm, CommentForm
from .models import Post, Comment, Category
from django.db.models import Count

# Home view
def home(request):
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/home.html', {'popular_posts': popular_posts, 'latest_posts': latest_posts})

# news index

def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    sort_by = request.GET.get('sort_by', 'time')
    if category_id:
        posts = Post.objects.filter(category_id=category_id)
    else:
        posts = Post.objects.all()
    if sort_by == 'popularity':
        posts = posts.annotate(num_comments=Count('comments')).order_by('-num_comments', '-created_at')
    elif sort_by == 'category':
        posts = posts.order_by('category', '-created_at')
    else:
        posts = posts.order_by('-created_at')


    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/index.html', {'posts': posts, 'categories': categories, 'popular_posts': popular_posts, 'latest_posts': latest_posts, 'page_obj': page_obj,})

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
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/create_post.html', {'form': form, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

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
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/post_form.html', {'form': form, 'post': post, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/delete_post.html', {'post': post, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

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
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/post_detail.html', {'post': post, 'comments': comments, 'form': form, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

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
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/edit_comment.html', {'form': form, 'comment': comment, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post_detail', slug=comment.post.slug)
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        return redirect('post_detail', slug=post_slug)
    return render(request, 'news/delete_comment.html', {'comment': comment, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

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
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'news/account_settings.html', {'popular_posts': popular_posts, 'latest_posts': latest_posts})

#user account functions

@login_required
def change_password(request):
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('account_profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

@login_required
def change_username(request):
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            request.user.username = form.cleaned_data['username']
            request.user.save()
            return redirect('account_profile')
    else:
        form = ChangeUsernameForm(initial={'username': request.user.username})
    return render(request, 'account/change_username.html', {'form': form, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

@login_required
def change_email(request):
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('account_profile')
    else:
        form = ChangeEmailForm(initial={'email': request.user.email})
    return render(request, 'account/change_email.html', {'form': form, 'popular_posts': popular_posts, 'latest_posts': latest_posts})

@login_required
def delete_account(request):
    popular_posts = Post.objects.annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:5]
    latest_posts = Post.objects.order_by('-created_at')[:5]
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            request.user.delete()
            return redirect('account_logout')
    else:
        form = DeleteAccountForm()
    return render(request, 'account/delete_account.html', {'form': form, 'popular_posts': popular_posts, 'latest_posts': latest_posts})



