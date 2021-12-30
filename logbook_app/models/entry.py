from django.db import models
from .logbook  import Logbook

class Entry(models.Model):
    id 					= models.AutoField(primary_key = True)
    logbook				= models.ForeignKey(Logbook, on_delete=models.CASCADE)
    date                = models.DateField()
    physichologist      = models.CharField(max_length=150)
    attendance          = models.BooleanField(default=False)
    description         = models.TextField(max_length=1000, null=True)
    satisfaction        = models.IntegerField(null=True)