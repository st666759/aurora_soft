from django.db import models

# Create your models here.

class cabine(models.Model):
    cabine_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    ubication = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 15, decimal_places=2)
    status = models.BooleanField(default=True)
    
    def _str_(self):
        return self.name