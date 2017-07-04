from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    # ex: /projects/
    url(r'^$', views.IndexView, name='index'),
    # ex: /projects/page/2
    url(r'^page/(?P<page>[0-9]+)/$', views.IndexView, name='indexI'),
    # ex: /projects/organization
    url(r'^organizations/$', views.Organizations, name='organizations'),
    # ex: /projects/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView, {'tab':'detail'}, name='detail'),
    # ex: /projects/1/instructions
    url(r'^(?P<pk>[0-9]+)/instructions/$', views.DetailView, {'tab':'instructions'}, name='instructions'),
    # ex: /projects/1/blog
    url(r'^(?P<pk>[0-9]+)/blog/$', views.DetailView, {'tab': 'blog'}, name='blog'),
    # ex: /projects/1/edit/
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /projects/1/edit/instruction/
    url(r'^(?P<pk>[0-9]+)/edit/steep/$', views.editSteep, name='addSteep'),
    # ex: /projects/1/edit/instruction/2/
    url(r'^(?P<pk>[0-9]+)/edit/steep/(?P<steep>[0-9]+)/$', views.editSteep, name='editSteep'),
    # ex: /projects/create
    url(r'^create/$', views.edit, name='create'),
    # ex: /projects/tests
    url(r'^tests/$', views.tests, name='tests'),
]
