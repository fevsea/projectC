from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    # ex: /projects/
    url(r'^$', views.IndexView, {'page': 1}, name='index'),
    # ex: /projects/page/2
    url(r'^page/(?P<page>[0-9]+)/$', views.IndexView, name='indexI'),
    # ex: /projects/detail/1/
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'),
    # ex: /projects/detail/1/edit/
    url(r'^detail/(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /projects/a
    url(r'^create/$', views.create, name='create'),
    # ex: /projects/tests
    url(r'^tests/$', views.tests, name='tests'),
]
