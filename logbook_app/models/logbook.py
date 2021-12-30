from django.db import models

class Logbook(models.Model):
	username				= models.CharField(unique=True, primary_key= True,max_length=150)
	creation_date           = models.DateField(auto_now_add=True)
