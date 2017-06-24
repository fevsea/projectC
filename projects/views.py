from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.conf import settings
from django.http import Http404

# Create your views here.

def index(request):
    """
       Main page of app

       **Template:**

       :template:`projects/base.html`
       """

    return render(request, 'projects/base.html')

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