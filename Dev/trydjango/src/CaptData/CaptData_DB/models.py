from django.db import models

# Create your models here.

class CaptData_Tbl(models.Model):
	
	Capt_ID 	= models.CharField(blank=False,max_length=50)
	Capt_Data 	= models.CharField(blank=False,max_length=1000)
