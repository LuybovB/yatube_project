
from sre_parse import expand_template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Post, Group

# Главная страница
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, template, context)

def group_posts(request):
    template = 'posts/group_posts.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }    
    return render(request, template, context)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)