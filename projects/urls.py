from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    # ex: /projects/
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    # ex: /projects/5/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /projects/tests
    url(r'^tests/$', views.tests, name='tests'),
]

