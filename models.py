from django.db import models
class permission(models.Model):
	PatientName=models.CharField(max_length=50)
	Medicaldetails=models.CharField(max_length=50)
	medicalhistory=models.CharField(max_length=40)
	treatementprovided=models.CharField(max_length=40)
