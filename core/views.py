from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Post, Category


def home(request):
    post_list = Post.objects.all()
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
        context['post_list'] = Post.objects.all()
        return context