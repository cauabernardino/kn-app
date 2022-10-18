from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer


@csrf_exempt
def shipments(request):
    """
    Handles `/shipments` endpoint actions.
    """
    if request.method == "GET":
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ShipmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shipments_specific(request, pk: int):
    """
    Handle `/shipments/{id}` endpoint actions.
    """
    try:
        task = Shipment.objects.get(pk=pk)
    except Exception:
        return HttpResponse(status=404)

    if request.method == "GET":
        shipment = Shipment.objects.get(id=pk)
        serializer = ShipmentSerializer(shipment, many=False)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ShipmentSerializer(task, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        task.delete()
        return HttpResponse(status=204)
