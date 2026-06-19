from django.db import models
from django.conf import settings

class Route(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='routes'
    )
    date = models.DateField()
    total_km = models.DecimalField(max_digits=8, decimal_places=2)
    fuel_cost = models.DecimalField(max_digits=8, decimal_places=2)
    gross_earnings = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='routes'

    def __str__(self):
        return f"Route {self.id} - {self.date}"


