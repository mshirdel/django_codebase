from django.http import HttpResponseRedirect


REDIRECT_FIELD_NAME = 'next'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def my_login_required(function=None):
    def wrapper(request, *args, **kw):
        user = request.user
        if not (user.id and request.session.get('code_success')):
            return HttpResponseRedirect('/ua/Sign In/')
        else:
            return function(request, *args, **kw)

    return wrapper
