from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^main_test/$', views.main, name='main'),  # need to modify the url !!!
    url(r'^accounts/signup/$', views.signup, name='signup'),
]