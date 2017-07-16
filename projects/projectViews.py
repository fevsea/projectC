from pprint import pprint

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max

from django.views import generic

from projects.forms import ProjectForm, SteepForm, BlogForm
from projects.models import Project, BuildSteep, Organization, BlogEntry

def DetailView(request, pk, tab='detail'):

    if not tab in ['detail', 'instructions', 'blog']:
        raise Http404
    p = get_object_or_404(Project, pk=pk)

    c = {'project': p, 'tab': tab}
    return render(request, 'projects/projectView.html', c)

def deleteBlog(request, pk, entry):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        p = get_object_or_404(Project, pk=pk)
        e = get_object_or_404(BlogEntry, pk=entry)
        e.delete()
        return HttpResponseRedirect(reverse("projects:blog", kwargs={'pk': pk}))

    else:
        raise Http404

def editBlog(request, pk, entry=None):
    e=None
    p=None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BlogForm(request.POST, request.FILES)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            p = get_object_or_404(Project, pk=pk)
            s = None
            try:
                date = form.cleaned_data['pub_date']
            except:
                date = None
            if form.cleaned_data['pub_date']:
                date = form.cleaned_data['pub_date']
            if entry is None:
                s = BlogEntry(project=p,
                            content=form.cleaned_data['content'],
                            title=form.cleaned_data['title'],
                            image=form.cleaned_data['image'],
                            pub_date= date
                            )
            else:
                s = p.blogentry_set.get(pk=entry)
                s.content = form.cleaned_data['content']
                s.title = form.cleaned_data['title']
                if date is not None:
                    s.pub_date = date
                if form.cleaned_data['image'] is not None:
                    s.image = form.cleaned_data['image']
            if form.cleaned_data['clear']:
                s.image = None
            s.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("projects:blog", kwargs={'pk': p.pk}))
        raise Http404

    # if a GET (or any other method) we'll create a blank form
    else:
        p = get_object_or_404(Project, pk=pk)
        if entry is not None:
            e = p.blogentry_set.get(pk=entry)
            data = {'content': e.content, 'title': e.title, 'pub_date': e.pub_date}
            form = BlogForm(data)
        else:
            data = {'pub_date': timezone.now()}
            form = BlogForm(data)

    context = {'form': form, 'project': p, 'entry': e}
    return render(request, 'projects/editBlog.html', context)