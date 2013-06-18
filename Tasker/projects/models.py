from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# from django.utils import timezone,date
# import datetime
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50, unique= True)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        #if not self.id:
            # Newly created object, so set slug
        str_slug = '%s %s' % (self.user.username,self.name)
        self.slug = slugify(str_slug)

        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    # def ending_recently(self):
    #      return self.end_date <= date.now() + date.timedelta(days=3)
    # ending_recently.admin_order_field = 'end_date'
    # ending_recently.boolean = True
    # ending_recently.short_description = 'Ending recently?'    

