from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField


User = get_user_model()


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    overview = models.CharField(max_length=60, null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    thumbnail = models.ImageField(upload_to='media/thumbnails', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=800)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -- {}'.format(self.author, self.post)


