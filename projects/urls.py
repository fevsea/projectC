from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    # ex: /projects/
    url(r'^$', views.IndexView, {'page': 1}, name='index'),
    # ex: /projects/page/2
    url(r'^page/(?P<page>[0-9]+)/$', views.IndexView, name='indexI'),
    # ex: /projects/5/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /projects/tests
    url(r'^tests/$', views.tests, name='tests'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'),
]

{'foo': 'bar'}