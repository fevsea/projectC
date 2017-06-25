from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class ProjectTemplate(models.Model):
    """
        Project and Courses common template
    """
    title = models.CharField(verbose_name=_('project title'), max_length=200, help_text=_("This will appear as the main project title"))
    brief_description = models.TextField(_('brief description'), help_text=_("Very short descrition. Will appear on project listing."))
    pub_date = models.DateTimeField(_('date published'), default=timezone.now)
    thumbnail = models.ImageField(upload_to='projects/thumbnail/')



    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Project(ProjectTemplate):
    """
        Represents a project
    """
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')