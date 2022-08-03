
from django.db import models


# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bed = models.IntegerField()
    num_bath = models.IntegerField()
    sq_ft = models.IntegerField()
    address = models.CharField(max_length=150)
    images = models.ImageField()

    def __str__(self):
        return self.title
