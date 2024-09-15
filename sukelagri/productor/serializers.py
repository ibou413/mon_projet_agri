from rest_framework import serializers
from .models import Farm, ProductorProfile, Crop, Sensor, SensorData, DataAnalysis, StatisticalReport, Dashboard


from rest_framework import serializers
from .models import CustomUser, Farm, WeatherForecast

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = '__all__'




class ProductorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductorProfile
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class DataAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnalysis
        fields = '__all__'

class StatisticalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticalReport
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'
