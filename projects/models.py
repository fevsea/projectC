from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _



class Project(models.Model):
    """
        Represents a project
    """

    title = models.CharField(verbose_name=_('title'), max_length=60, help_text=_("Title used for listing"))
    summary = models.CharField(_('brief description'),  max_length=140, help_text=_("Very short descrition. Will appear on project listing."))
    description = models.TextField(_('description'),  help_text=_("Desciption of the project (not actually explanation)"))
    details = models.TextField(_('details'),  help_text=_("Full explanation of the project)"))
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    update_date = models.DateTimeField(_('last update date'), auto_now=True )
    thumbnail = models.ImageField(upload_to='projects/thumbnail/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')



class BuildSteep(models.Model):
    """
        One of the steps on the individual items of the instructions
    """

    project = models.ForeignKey('Project',
        on_delete=models.CASCADE,
    )
    content = models.TextField(_('steep content'), help_text=_("Explanation of one individual step on the elavoration fo the project"))
    number = models.IntegerField(_("position on steep list"))


    def __str__(self):
        return self.number.__str__()

    class Meta:
        verbose_name = _('project steep')
        verbose_name_plural = _('project steeps')
