from django.db import models


class Developers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Documente_number=models.CharField(max_length=200)
    Language_Develop = models.CharField(max_length=200)
    Experience = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    years = models.IntegerField()
    
    