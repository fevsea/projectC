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

from projects.forms import ProjectForm, SteepForm
from projects.models import Project, BuildSteep, Organization


def IndexView(request, page=1):
    """
       Main page of app

       **Template:**

       :template:`projects/index.html`
    """
    project_list = Project.objects.filter(
        update_date__lte=timezone.now()
        ).order_by('-update_date')
    paginator = Paginator(project_list, 2)

    pass

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    return render(request, 'projects/index.html', {'projects': projects})


class DetailView(generic.DetailView):
    """
       Detalled view of a :model:`projects.Project`.


       **Template:**

       :template:`project/detail.html`
       """
    model = Project
    template_name = 'projects/detail.html'


def Organizations(request, page=1):
    """
       Main page of app

       **Template:**

       :template:`projects/index.html`
    """
    organizations = Organization.objects.all().order_by('name')

    return render(request, 'projects/organizations.html', {'organizations': organizations})

def tests(request):
    """
       Used for development convenience.
       THIS SHOULD DISAPPEAR WHEN CODE IS OFFICIALLY RELASED


       **Template:**

       :template:`projects/tests.html`
       """
    if not settings.DEBUG:
        raise Http404


    c = {
        "title": _("tests"),
        "second": "second",
        "tt": request,
        "float": 123123.230
    }
    return render(request, 'projects/tests.html', c)

def edit(request, pk=None):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            p = None
            if pk is None:
                p = Project(title=form.cleaned_data['title'],
                            summary=form.cleaned_data['summary'],
                            description=form.cleaned_data['description'],
                            details=form.cleaned_data['details'],
                            thumbnail="projects/thumbnail/default.png")
            else:

                p = get_object_or_404(Project, pk=pk)
                p.title=form.cleaned_data['title']
                p.summary=form.cleaned_data['summary']
                p.description=form.cleaned_data['description']
                p.details=form.cleaned_data['details']
                #thumbnail=form.cleaned_data['thumbnail']

            p.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("projects:detail", kwargs={'pk': p.pk}))

    # if a GET (or any other method) we'll create a blank form
    else:
        if pk is not None:
            p = get_object_or_404(Project, pk=pk)
            data = {'title': p.title,
                    'summary': p.summary,
                    'description': p.description,
                    'details': p.details,
                    #'thumbnail': p.thumbnail
                    }
            form = ProjectForm(data)
        else:
            form = ProjectForm

    return render(request, 'projects/editProject.html', {'form': form, 'pk':pk})


def editSteep(request, pk, steep=None):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SteepForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            p = get_object_or_404(Project, pk=pk)
            if steep is None:
                pos = p.buildsteep_set.aggregate(Max('number'))['number__max']
                pos = pos if pos is not None else 0
                s = BuildSteep(project=p,
                            content=form.cleaned_data['content'],
                               number=pos+1
                            )
            else:
                s = p.buildsteep_set.get(pk=steep)
                s.content = form.cleaned_data['content']

            s.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("projects:detail", kwargs={'pk': p.pk}))

    # if a GET (or any other method) we'll create a blank form
    else:
        if steep is not None:
            p = get_object_or_404(Project, pk=pk)

            data = {'content': p.buildsteep_set.get(pk=steep).content}
            form = SteepForm(data)
        else:
            form = SteepForm

    return render(request, 'projects/editSteep.html', {'form': form, 'pk':pk})