from django.db import models

# Create your models here.

class CeleryStatus(models.Model):
    task_id = models.CharField(max_length=64, unique = True, null=False, blank=False)
    status = models.CharField(max_length=32, null=False, blank=False)
    arguments = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.task_id + ":" + self.status