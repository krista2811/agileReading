from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^main_test/$', views.main, name='main'),  # need to modify the url !!!
    url(r'^accounts/signup/$', views.signup, name='signup'),
    url(r'^main_test/report_edit/(?P<slug>[-\w]+)/$', views.report_edit, name='report_edit'),
    url(r'^main_test/book_list/$', views.book_list, name='book_list'),
    url(r'^main_test/report_list/(?P<slug>[-\w]+)/$', views.report_list, name='report_list'),
    url(r'^main_test/report_contents/(?P<slug>[-\w]+)/$', views.report_contents, name='report_contents'),
]