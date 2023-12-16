from .models import Category


def category_sidebar(request):
    return {'category_list': Category.objects.all()}
