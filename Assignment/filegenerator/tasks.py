from itertools import count
import os
import csv

from celery import shared_task, current_task
from celery.result import AsyncResult

from essential_generators import DocumentGenerator

from Assignment.celery import app

from .models import * 


@shared_task(name='file_generator')
def file_generator(file_name, data_count):
    """
    Function for creating the text for csv file.
    """
    # Initially storing the required data to track the status.
    args = "Filename:" + file_name + "," + "Sentence count:" + str(data_count)
    CeleryStatus.objects.create(
        task_id=current_task.request.id, status="PENDING", arguments=args)

    sentence_list = []
    for a in range(data_count):
        a = DocumentGenerator().sentence().replace(",", "")
        sentence_list.append([a])
    csv_writer(file_name, sentence_list)


def csv_writer(file_name, data_list):
    """
    Function to create a csv file.
    """
    file_name = str(os.path.dirname(os.path.abspath(__file__)) + "/../data/") + file_name + ".csv"
    with open(file_name, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerows(data_list)


@shared_task(name='update_task_status')
def update_task_status():
    """
    Updating the status of the functions in 10 sec intervals.
    """
    for status_instance in CeleryStatus.objects.filter(status='PENDING'):
        _state = AsyncResult(status_instance.task_id).state
        status_instance.status = _state
        status_instance.save()
