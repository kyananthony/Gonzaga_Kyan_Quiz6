from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'base.html')
@login_required
def create_post(request):
    try:
        post = Post.objects.get(user=request.user)
        return render(request, 'posts/post_exist.html', {'post': post})
    except Post.DoesNotExist:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.save()
                return redirect('post_success')  # Ensure this URL is defined
        else:
            form = PostForm()
        return render(request, 'posts/create_post.html', {'form': form})