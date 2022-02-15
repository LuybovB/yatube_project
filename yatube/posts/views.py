from sre_parse import expand_template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)

def group_posts(request):
    template = 'posts/group_posts.html'
    posts = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'posts': posts,
    }    
    return render(request, template, context)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)