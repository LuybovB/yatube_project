from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница сообщества
def group_posts(request, slug):
    return HttpResponse(f'Страница сообщества {slug}')

