import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Country

__author__ = 'awesome'


@csrf_exempt
def home(request):
    string = request.POST['text']
    country = Country.is_valid(string)
    if country:
        response = {"valid": "valid", "country": country.name}
    else:
        response = {"valid": "invalid"}
    return HttpResponse(json.dumps(response), content_type="application/json")