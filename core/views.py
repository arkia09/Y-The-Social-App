from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

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
    return render(request, 'post_create.html', context)

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
    return render(request, 'post_create.html', context)

    
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk= post_id, user = request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete_confirmation.html', {'post': post})

@login_required
def toggle_likes(request, post_id):
    post = get_object_or_404(Post, id=  post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked= False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponse(f"""
    <button 
        hx-post="/post/{post.id}/like/htmx/" 
        hx-target="#like-btn-{post.id}" 
        hx-swap="outerHTML"
        class="flex items-center space-x-1">
        
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 {'text-red-600 fill-current' if liked else 'text-gray-500'}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364
                     l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636
                     l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
        </svg>
        <span id="like-count-{post.id}" class="text-sm font-medium">{post.likes.count}</span>
    </button>
    """
    )