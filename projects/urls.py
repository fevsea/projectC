from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    # ex: ~/
    url(r'^$', views.IndexView, name='index'),
    # ex: ~/page/2
    url(r'^page/(?P<page>[0-9]+)/$', views.IndexView, name='indexI'),
    # ex: ~/organization
    url(r'^organizations/$', views.Organizations, name='organizations'),
    # ex: ~/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView, {'tab':'detail'}, name='detail'),
    # ex: ~/1/instructions
    url(r'^(?P<pk>[0-9]+)/instructions/$', views.DetailView, {'tab':'instructions'}, name='instructions'),

    # ex: ~/1/blog
    url(r'^(?P<pk>[0-9]+)/blog/$', views.DetailView, {'tab': 'blog'}, name='blog'),
    # ex: ~/1/blog/create
    url(r'^(?P<pk>[0-9]+)/blog/create/$', views.editBlog, name='addBlog'),
    # ex: ~/1/blog/edit/1
    url(r'^(?P<pk>[0-9]+)/blog/(?P<entry>[0-9]+)/edit/$', views.editBlog, name='editBlog'),
    # ex: ~/1/edit/
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: ~/1/edit/instruction/
    url(r'^(?P<pk>[0-9]+)/edit/steep/$', views.editSteep, name='addSteep'),
    # ex: ~/1/edit/instruction/2/
    url(r'^(?P<pk>[0-9]+)/edit/steep/(?P<steep>[0-9]+)/$', views.editSteep, name='editSteep'),
    # ex: ~/create
    url(r'^create/$', views.edit, name='create'),
    # ex: ~/tests
    url(r'^tests/$', views.tests, name='tests'),
]
