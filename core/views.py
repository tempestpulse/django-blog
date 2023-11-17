from django.shortcuts import render
from .models import Post


def home(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list
    }

    return render(request, 'core/index.html', context)
