from django.db import models
from django.utils import timezone
import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.timezone import now
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _



class Project(models.Model):
    """
        Represents a project
    """

    title = models.CharField(verbose_name=_('title'), max_length=60, help_text=_("Title used for listing"))
    summary = models.CharField(_('brief description'),  max_length=140, help_text=_("Very short descrition. Will appear on project listing."))
    description = tinymce_models.HTMLField(_('description'),  help_text=_("Desciption of the project (not actually explanation)"))
    details = tinymce_models.HTMLField(_('details'),  help_text=_("Full explanation of the project)"), blank=True, null=True)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    update_date = models.DateTimeField(_('last update date'), auto_now=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnail/', blank=True, null=True)
    mainProject = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)

    @property
    def thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')



class BuildSteep(models.Model):
    """
        One of the steps on the individual items of the instructions
    """
    name = models.CharField(max_length=64, blank=True)
    project = models.ForeignKey('Project',
        on_delete=models.CASCADE,
    )
    content = tinymce_models.HTMLField(_('steep content'), help_text=_("Explanation of one individual step on the elavoration fo the project"))
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)


    def __str__(self):
        return self.name.__str__()

    class Meta:
        verbose_name = _('project steep')
        verbose_name_plural = _('project steeps')

class Organization(models.Model):
    """
        An organization hav projects. Pex. and IEEE student branch
    """

    name = models.CharField(verbose_name=_('name'), max_length=128)
    university = models.CharField(max_length=64, blank=True, null=True)
    ieee = models.BooleanField()
    website = models.CharField(max_length=256, blank=True, null=True)
    facebook = models.CharField(max_length=128, blank=True, null=True)
    twitter = models.CharField(max_length=128, blank=True, null=True)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    update_date = models.DateTimeField(_('last update date'), auto_now=True)
    logo = models.ImageField(upload_to='projects/organization/', blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')


class Resource(models.Model):
    """
        Resource unit. Allow an easy resource manager implementstion.
    """
    FILE_TYPE = (
        ('IMG', 'image'),
        ('COD', 'code'),
        ('DOC', 'document'),
        ('FIL', 'other'),
        ('WEB', 'website'),
    )

    project = models.ForeignKey('Project', on_delete=models.CASCADE )

    buildSteep = models.ForeignKey('BuildSteep', on_delete=models.CASCADE, null=True, blank=True)
    blogEntry = models.ForeignKey('BlogEntry', on_delete=models.CASCADE, null=True, blank=True)


    name = models.CharField(verbose_name=_('name'), max_length=64, blank=True, null=True)
    type = models.CharField(max_length=3, choices=FILE_TYPE)
    file = models.FileField(upload_to='projects/steeps/' ,blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects/generated', editable=False, blank=True, null=True)
    special_type = models.CharField(max_length=32, blank=True, null=True)
    url = models.CharField(verbose_name=_('url'), max_length=512, blank=True, null=True)

    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url

    def save(self, *args, **kwargs):

        if self.type == 'IMG' and not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(Resource, self).save(*args, **kwargs)


    def make_thumbnail(self):
        image = Image.open(self.file)


        thumb_name, thumb_extension = os.path.splitext(self.file.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Crrop image at 10:25 ration
        image.thumbnail((500, 200), Image.ANTIALIAS)
        width = image.size[0] / 2
        height = image.size[1] / 2
        targetWidth = width
        if 2.5*height < targetWidth:
            targetWidth = 2.5 * height
        targetHeight = targetWidth/2.5

        image = image.crop(
            (
                int(round(width/2 - targetWidth/2)),
                int(round(height/2 - targetHeight/2)),
                int(round(width/2 + targetWidth/2)),
                int(round(height/2 + targetHeight/2))
            )
        )

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('resource')
        verbose_name_plural = _('resources')


class BlogEntry(models.Model):
    """
        Blog entry.
    """

    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=128)
    content = tinymce_models.HTMLField(_('blog entry content'))
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    pub_date = models.DateTimeField(default=now)

    @property
    def is_after_publish_date(self):
        return self.pub_date <= now()


    def __str__(self):
        if self.title is None or self.title == "":
            return str(self.pub_date)
        return self.title

    class Meta:
        verbose_name = _('blog entry')
        verbose_name_plural = _('blog entries')




