from rest_framework import viewsets
from .models import Farm, ProductorProfile, Crop, Sensor, SensorData, DataAnalysis, StatisticalReport, Dashboard
from .serializers import FarmSerializer, ProductorProfileSerializer, CropSerializer, SensorSerializer, SensorDataSerializer, DataAnalysisSerializer, StatisticalReportSerializer, DashboardSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class ProductorProfileViewSet(viewsets.ModelViewSet):
    queryset = ProductorProfile.objects.all()
    serializer_class = ProductorProfileSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

class DataAnalysisViewSet(viewsets.ModelViewSet):
    queryset = DataAnalysis.objects.all()
    serializer_class = DataAnalysisSerializer

class StatisticalReportViewSet(viewsets.ModelViewSet):
    queryset = StatisticalReport.objects.all()
    serializer_class = StatisticalReportSerializer

class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
