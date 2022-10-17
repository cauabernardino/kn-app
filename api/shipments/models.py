from django.db import models


class Shipment(models.Model):
    """Model for a shipment."""

    description = models.TextField(max_length=100, null=False)
    destination = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.due_date} - {self.destination} - {self.description}"