from audioop import max

from django.db import models


# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=300)
    gen_name = models.CharField(max_length=100)
    size = models.IntegerField()
    content_type = models.CharField(max_length=100)
    extension = models.CharField(max_length=30)

    class Meta:
        db_table = "uploads"
