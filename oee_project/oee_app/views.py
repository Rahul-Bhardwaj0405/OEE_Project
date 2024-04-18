from django.shortcuts import render

# Create your views here.
# oee_app/views.py

from rest_framework import viewsets
from .models import Machines, ProductionLog
from .serializers import MachinesSerializer, ProductionLogSerializer

class MachinesViewSet(viewsets.ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachinesSerializer

class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer
