from datetime import datetime

from django.test import TestCase

from shipments import models


class ModelTests(TestCase):
    def test_shipment_str(self):
        """should display the shipment as string"""
        ship = models.Shipment.objects.create(
            description="30 Televisions",
            destination="OPO",
            due_date=datetime(2022, 12, 25)
        )

        self.assertEqual(
            str(ship),
            f"{ship.due_date} - {ship.destination} - {ship.description}"
        )
