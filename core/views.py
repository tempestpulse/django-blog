from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .forms import PostForm
from .models import Post, Category, Comment


def home(request):
    post_list = Post.objects.order_by('timestamp')
    category_list = Category.objects.all()
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'category_list': category_list,
        'page_obj': page_obj
    }

    return render(request, 'core/index.html', context)


class PostDetail(DetailView):
    model = Post
    template_name = 'core/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


def search(request):
    category_list = Category.objects.all()
    if request.method == 'GET':
        search_input = request.GET.get('q')
        post_list = Post.objects.filter(title__icontains=search_input)

        context = {
            'category_list': category_list,
            'search_input': search_input,
            'post_list': post_list
        }
        return render(request, 'core/search_result.html', context)


def category_browse(request, category_id):
    category_list = Category.objects.all()
    category_selected = get_object_or_404(Category, id=category_id)
    post_list = Post.objects.filter(category=category_selected)

    context = {
        'post_list': post_list,
        'category_list': category_list
    }

    return render(request, 'core/category_result.html', context)


@login_required
def add_post(request):
    category_list = Category.objects.all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post-detail', pk=new_post.id)
    context = {
        'category_list': category_list,
        'form': form
    }

    return render(request, 'core/add_post.html', context)
