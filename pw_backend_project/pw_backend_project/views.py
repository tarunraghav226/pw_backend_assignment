import json
from urllib.request import Request

from django.core import serializers
from django.http import HttpResponse

from .models import CustomUser
from helpers.authentication_helper import AuthenticationHelper


authentication_helper = AuthenticationHelper()

def sign_up_user(request: Request):
    if request.method != "POST":
        data = {
            "status": 400,
            "detail": "Only POST request allowed"
        }
        return HttpResponse(json.dumps(data), status=400, content_type='application/json')

    hashed_password = authentication_helper.get_hashed_password("123435")
    user = CustomUser(
                    phone_number="12356", 
                    passowrd=hashed_password
                )
    user.save()

    data = serializers.serialize('json', [user,])
    struct = json.loads(data)
    data = json.dumps(struct[0]['fields'])
    return HttpResponse(data, content_type='application/json')
