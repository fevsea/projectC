from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from projects.models import Project, BuildSteep, Organization, BlogEntry, Resource
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    model = BuildSteep
    extra = 0  # Cannot be deleted

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')
    fieldsets = [
        (None, {'fields': ['title', 'summary', 'thumbnail', 'organization']}),
        (_('Content'), {'fields': ['description', 'details']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['creation_date']  # Filter sidebar
    search_fields = ['title']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Organization)
admin.site.register(BlogEntry)
admin.site.register(BuildSteep)
admin.site.register(Resource)

admin.site.site_header = _('ProjectC administration')
admin.site.site_title = _('ProjectC admin site')