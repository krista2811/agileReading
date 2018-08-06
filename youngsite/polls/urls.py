from django.conf.urls import url
from . import views


app_name = 'polls'
urlpatterns = [
    # polls/something
    # polls/ 는 youngsite.urls.py에 의해 정의되는 파트

    # path(route, view, kwargs=None, name=None)
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
