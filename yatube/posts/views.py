from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Главная страница
def index(request):
    # template = loader.get_template('posts/index.html')
    return render(request, 'posts/index.html')

# Страница сообщества
def group_list(request):
    # template = 'posts/group_list.html'
    return render(request, 'posts/group_list.html')