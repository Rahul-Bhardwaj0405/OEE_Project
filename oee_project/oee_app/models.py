from django.db import models

# Create your models here.
# oee_app/models.py

from django.db import models

class Machines(models.Model):
    machine_name = models.CharField(max_length=255)
    machine_serial_no = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

class ProductionLog(models.Model):
    cycle_no = models.CharField(max_length=20)
    unique_id = models.UUIDField(unique=True)
    material_name = models.CharField(max_length=255)
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()
