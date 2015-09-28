from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^Sign In/', views.sign_in, name='sign_in'),
    url(r'^Logout/', views.logout_user, name='logout_user'),
    url(r'^Sign Up/', views.sign_up, name='sign_up')
]