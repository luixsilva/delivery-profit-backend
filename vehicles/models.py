from django.db import models
from django.conf import settings

class Vehicle (models.Model):

    class FuelType(models.TextChoices):
        GASOLINE = 'gasoline', 'Gasolina'
        ETHANOL = 'ethano', 'Etanol'
        FLEX = 'flex', 'Flex',
        DIESEL = 'diesel', 'Diesel'



    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    fuel_type = models.CharField(
        max_length=20,
        choices= FuelType.choices
    )
    consumption = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'vehicles'

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"
     