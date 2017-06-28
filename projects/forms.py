from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from projectC.settings import TINYMCE_DEFAULT_CONFIG


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=60);
    summary = forms.CharField(max_length=140);
    description =  forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))
    details = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 60}))
    #thumbnail = forms.ImageField()


class SteepForm(forms.Form):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))