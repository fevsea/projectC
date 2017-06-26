from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.conf import settings
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import generic
from projects.models import Project


def IndexView(request, page):
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