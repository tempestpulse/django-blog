from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, CommentForm, RegisterForm
from .models import Post, Category


def home(request):
    post_list = Post.objects.order_by('timestamp')
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'post_list': post_list,
        'page_obj': page_obj
    }

    return render(request, 'core/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Post.objects.filter(pk=pk).update(view_count=F('view_count') + 1)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'core/post.html', context)


def search(request):
    if request.method == 'GET':
        search_input = request.GET.get('q')
        post_list = Post.objects.filter(title__icontains=search_input)

        context = {
            'search_input': search_input,
            'post_list': post_list
        }
        return render(request, 'core/search_result.html', context)


def category_browse(request, category_id):
    category_selected = get_object_or_404(Category, id=category_id)
    post_list = Post.objects.filter(category=category_selected)

    return render(request, 'core/category_result.html', {'post_list': post_list})


@login_required
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post-detail', pk=new_post.id)

    return render(request, 'core/add_post.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Login failed, try again')
            return redirect('login')
    else:
        return render(request, 'core/login.html')


def register(request):
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'core/register.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')
