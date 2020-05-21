from django.db import models

# Create your models here.

class Emplyee(models.Model):
    E_name = models.CharField(max_length=50)
    E_Id = models.CharField(max_length=50, unique=True)
    E_address = models.CharField(max_length=50)
    E_salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.E_name