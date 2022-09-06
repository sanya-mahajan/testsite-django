from unicodedata import name
from unittest.result import failfast
from django.db import models
from django import forms

# Create your models here.

class data(models.Model):  #table
    name=models.CharField(max_length=20,unique=True,null=False)
    quote=models.TextField(max_length=1000,null=False)
    adjective=models.CharField(max_length=50)
    date=models.DateField()

    #to give the entry name the person's name
    def __str__(self):
        entryname=self.name+' '+self.adjective
        return entryname

class mood(forms.Form):
    mood_field=forms.CharField(label="how you feel'in?")