from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 40)
    email = models.EmailField()
    contra = models.CharField(max_length = 30)
    
class Roms(models.Model):
    nombre = models.CharField(max_length = 100)
    
    
class Emuladores(models.Model):
    nombre = models.CharField(max_length = 100)
    

    