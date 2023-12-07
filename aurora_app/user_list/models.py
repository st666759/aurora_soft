from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo = models.EmailField()
    status = models.BooleanField(default=True)
    


    def __str__(self):
        return self.name


