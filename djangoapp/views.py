#Django
from djangoapp.settings import DEBUG
from django.http import HttpResponse

#utilities
from datetime import datetime
import json

def hello_world(request):
    time_now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Current time sever is: {time_now}')

def sorted_numbers(request):

    numbers = [int(n) for n in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)

    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integer sorted succesfully.'
    }
    return HttpResponse(json.dumps(data, indent = 4), content_type="application/json")

def say_hi(request,name,age):

    #return a greeting
    if age < 12:
        message = f'Sorry {name},you are not allowed here.'
    else:
        message = f'Welcome {name}'

    return HttpResponse(message, content_type="text/plain")
