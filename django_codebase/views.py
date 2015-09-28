from django.shortcuts import render


def index(request):
    context = {'home_page_data': 'Hello Django!'}
    return render(request, 'django_codebase/index.html', context)
