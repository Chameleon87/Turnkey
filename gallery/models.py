from django.db import models
from django.contrib.auth.models import User
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from PIL import Image as PImage
from settings import MEDIA_ROOT
from string import join
import os

class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=True)
    cover_photo = models.ForeignKey('Image', blank=True, null=True)

    def __unicode__(self):
        return self.title
    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["{{ media_url }}" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')

    images.allow_tags = True

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to="images/")
    thumbnail = ImageSpecField([ResizeToFill(200, 120)], source='image', format='JPEG', options={'quality': 90})
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.image.name
    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        super(Image, self).save(*args, ** kwargs)

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def __unicode__(self):
        return self.image.name

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ', '))

    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return str(join(lst, ', '))
