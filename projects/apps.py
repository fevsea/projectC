from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class ProjectsConfig(AppConfig):
    name = 'projects'
    verbose_name = pgettext_lazy('app name (ie admin page)', 'projects')