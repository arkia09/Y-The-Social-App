from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'core/home.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form =  PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    context = {
        'form': form,
        "form_heading": 'Create a new post',
        'form_title': 'Create Post',
        'button_text': 'Create'    

    }
    return render(request, 'core/post_create.html', context)

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'form_heading': 'Edit your post',
        'button_text': 'Save Changes'
    }
    return render(request, 'core/post_create.html', context)

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk= post_id, user = request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'core/post_delete_confirmation.html', {'post': post})


def toggle_likes(request, post_id):
    if not request.user.is_authenticated:
        messages.info(request, "You are required to sign up or log in to like a post")
        return redirect('register')
    
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_list')


def add_comment(request, post_id):
    if not request.user.is_authenticated:
        messages.info(request, "You are required to sign up or log in to add a comment")
        return redirect('register')
    
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        body = request.POST.get("body")
        if body:
            Comment.objects.create(post=post, body=body, name=request.user.username)
    return redirect(request.META.get('HTTP_REFERER', 'post_list'))