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

def Organizations(request, page=1):
    """
       Main page of app

       **Template:**

       :template:`projects/index.html`
    """
    organizations = Organization.objects.all().order_by('name')

    return render(request, 'projects/organizations.html', {'organizations': organizations})


def DetailView(request, pk, tab="info"):
    tabs = ["info", "blog", "projects"]
    if tab not in tabs:
        raise Http404
    o = get_object_or_404(Organization, pk=pk)

    c = {'organization': o, 'tab': tab}
    return render(request, 'projects/organizationView.html', c)
