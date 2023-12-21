from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length = 40)
    email = models.EmailField()
    contra = models.CharField(max_length = 30)
    def __str__(self):
        return f'Nombre: {self.nombre}- Email: {self.email}- Contra: {self.contra}'
    
class Roms(models.Model):
    nombre = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100, )
    def __str__(self):
        return f"Nombre: {self.nombre}- Link: {self.link}"
    
class Emuladores(models.Model):
    nombre = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100, default="asd")
    def __str__(self):
        return f"Nombre:{self.nombre}- Link:{self.link}"
     
    
    

    
    

    