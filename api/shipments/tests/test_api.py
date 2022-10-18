from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer


SHIPMENTS_URL = "/api/shipments/"


class ShipmentAPITests(TestCase):
    """Tests for `/shipments` endpoint"""

    def setUp(self):
        self.client = APIClient()
        self.test_payload = {
            "description": "100 cellphones",
            "destination": "GRU",
            "due_date": "2023-01-20",
        }

    def test_retrieve_shipments(self):
        """should retrieve shipments"""
        Shipment.objects.create(
            description="30 Televisions",
            destination="OPO",
            due_date="2022-12-25"
        )

        Shipment.objects.create(
            description="50 Notebooks",
            destination="LIS",
            due_date="2023-01-20"
        )

        res = self.client.get(SHIPMENTS_URL, format="api")

        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json(), serializer.data)

    def test_create_shipment_successfully(self):
        """should create new shipment successfully"""

        res = self.client.post(SHIPMENTS_URL, self.test_payload, format="json")

        shipment_exists = Shipment.objects.filter(
            destination=self.test_payload["destination"]
        ).exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(shipment_exists)

    def test_not_reate_invalid_shipment(self):
        """should not allow to create a shipment with wrong values"""
        payload = {"destination": ""}

        res = self.client.post(SHIPMENTS_URL, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_shipment_successfully(self):
        """should update shipment successfully"""
        update_payload = {
            "description": "107 cellphones",
            "destination": "GRU",
            "due_date": "2023-01-25",
        }

        res_post = self.client.post(
            SHIPMENTS_URL, self.test_payload, format="json"
        )
        obj_id = res_post.json()["id"]

        res = self.client.put(
            f"{SHIPMENTS_URL}{obj_id}/", update_payload, format="json"
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(res.json(), update_payload)

    def test_delete_shipment_successfully(self):
        """should delete shipment successfully"""
        delete_payload = {
            "description": "1 golden bar",
            "destination": "CDG",
            "due_date": "2023-02-10",
        }
        res_post = self.client.post(
            SHIPMENTS_URL, delete_payload, format="json"
        )
        obj_id = res_post.json()["id"]

        res = self.client.delete(f"{SHIPMENTS_URL}{obj_id}/", format="json")

        shipment_exists = Shipment.objects.filter(
            destination=res_post.json()["destination"]
        ).exists()

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(shipment_exists)
