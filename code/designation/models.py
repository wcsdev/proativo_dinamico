from django.db import models

# Create your models here.

class Designacoe(models.Model):
    unidade = models.CharField(max_length=250, blank=False, null=False)
    designacao = models.CharField(max_length=250,blank=False, null=False)


    def __str__(self):
        return (f"{self.unidade} - {self.designacao}")
    
