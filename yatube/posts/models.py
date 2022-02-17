from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    def __str__(self):
        return f'{self.title}'

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=100)

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = 'posts') 
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name = 'posts',
        blank=True, null=True, max_length=100)