from django.http import HttpResponse
from django.template import loader

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница сообщества
def group_posts(request, slug):
    return HttpResponse(f'Страница сообщества {slug}')

def index(request):
    template = loader.get_template('posts/index.html')
    return HttpResponse(template.render({}, request))