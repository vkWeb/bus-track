from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from tracking.models import BusLocation


def index(request):
    return HttpResponse("API Server Running.")


@csrf_exempt
def bus_location(request):
    if request.method == "POST":
        bus_id = request.POST["bus_id"]
        bus_location = BusLocation.objects.get(pk=bus_id)

        bus_location.longitude = request.POST["longitude"]
        bus_location.latitude = request.POST["latitude"]
        bus_location.save()

    elif request.method == "GET":
        bus_id = request.GET["bus_id"]
        bus_location = BusLocation.objects.get(pk=bus_id)

        return JsonResponse({
            "bus_id": bus_id,
            "longitude": bus_location.longitude,
            "latitude": bus_location.latitude,
        })
