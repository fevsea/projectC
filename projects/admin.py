from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from projects.models import Project, BuildSteep


admin.site.register(Project)
admin.site.register(BuildSteep)

admin.site.site_header = _('ProjectC administration')
admin.site.site_title = _('ProjectC admin site')
