from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50, unique= True)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name