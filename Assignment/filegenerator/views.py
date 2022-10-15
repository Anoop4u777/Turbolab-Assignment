from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from celery.result import AsyncResult

from .tasks import file_generator
from .models import *

# Create your views here.


@api_view(["POST"])
def generate_file(request):
    """
    POSTDATA STRUCTURE:
    {
        "fileName": "test",
        "count": 20
    }
    """
    file_name = request.data.get("fileName", None)
    count = request.data.get("count", None)
    if any([file_name, count]) is None:
        raise ValidationError("File name and count is required to generate file")

    # Celery task to generate file
    file_generator.delay(file_name, count)
    
    return response.Response("Success")