from parsedatetime import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class ad_detail(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    details = models.CharField(max_length=1000)
    price = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

        def __str__(self):
            return  self.title



class Auction(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    startdate = models.DateTimeField(blank=False)
    enddate = models.DateTimeField(blank=False)
    status = models.CharField(max_length=20, default='active')
    seller = models.CharField(max_length=255, blank=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.title