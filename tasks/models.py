from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
from projects.models import Project
# Create your models here.


class Task(models.Model):
    PRIORITY_LIST = [ ('1',"High"), ('2',"Medium"), ('3',"Low"), ]

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.CharField( 
        max_length = 1,
        choices = PRIORITY_LIST)
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    slug = models.SlugField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.name)
    #     super(Task, self).save(*args, **kwargs)

    def save(self, **kwargs):
        slug_str = "%s %s" % (self.project, self.name) 
        self.slug = slugify (slug_str)
        super(Task, self).save()
   
    def __unicode__(self):
        return self.name + ":" + self.priority

