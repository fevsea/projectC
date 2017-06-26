from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from projects.models import Project, BuildSteep

class ChoiceInline(admin.TabularInline):
    model = BuildSteep
    extra = 0  # Cannot be deleted

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')
    fieldsets = [
        (None, {'fields': ['title', 'summary', 'thumbnail']}),
        (_('Content'), {'fields': ['description', 'details']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['creation_date']  # Filter sidebar
    search_fields = ['title']


admin.site.register(Project, ProjectAdmin)

admin.site.site_header = _('ProjectC administration')
admin.site.site_title = _('ProjectC admin site')