from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from datetimewidget.widgets import DateTimeWidget

from projectC.settings import TINYMCE_DEFAULT_CONFIG


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=60);
    summary = forms.CharField(max_length=140);
    description =  forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))
    details = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 60}), required=False)
    thumbnail = forms.ImageField()


class SteepForm(forms.Form):
    title = forms.CharField(max_length=64, required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))
    files = forms.formset_factory(forms.FileInput)
    
class ResourceForm(forms.Form):
    FILE_TYPE = (
        ('IMG', 'image'),
        ('COD', 'code'),
        ('DOC', 'document'),
        ('FIL', 'other'),
        ('WEB', 'website'),
    )


    name = forms.CharField()
    type = forms.CharField()
    file = forms.FileField()

class BlogForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))
    image = forms.ImageField(required=False)
    clear = forms.BooleanField(required=False)