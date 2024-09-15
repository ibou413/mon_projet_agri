from django.contrib import admin
from .models import CustomUser, Farm, WeatherForecast, ProductorProfile, Crop, Sensor, SensorData

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'location')
    search_fields = ('name', 'location')

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('farm', 'forecast_date', 'forecast_data')
    list_filter = ('forecast_date', 'farm')
    search_fields = ('farm__name',)

@admin.register(ProductorProfile)
class ProductorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'farm_name', 'location', 'contact_number')
    search_fields = ('user__email', 'farm_name', 'location')

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'planting_season', 'harvest_time')
    search_fields = ('name', 'planting_season', 'harvest_time')

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('farm', 'type', 'location', 'installation_date')
    list_filter = ('type', 'installation_date')
    search_fields = ('farm__farm_name', 'type', 'location')

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'timestamp', 'data')
    list_filter = ('sensor', 'timestamp')
    search_fields = ('sensor__type', 'data')

from django.contrib import admin
from .models import DataAnalysis, StatisticalReport, Dashboard

@admin.register(DataAnalysis)
class DataAnalysisAdmin(admin.ModelAdmin):
    # Affiche les champs 'farm', 'analysis_type', et 'analysis_date' dans la liste d'affichage
    list_display = ('farm', 'analysis_type', 'analysis_date')
    # Ajoute des filtres pour le type d'analyse et la ferme
    list_filter = ('analysis_type', 'farm')
    # Barre de recherche sur la ferme et le type d'analyse
    search_fields = ('farm__name', 'analysis_type')

@admin.register(StatisticalReport)
class StatisticalReportAdmin(admin.ModelAdmin):
    # Affiche les champs 'farm', 'report_type', et 'report_date' dans la liste d'affichage
    list_display = ('farm', 'report_type', 'report_date')
    # Ajoute des filtres pour le type de rapport et la ferme
    list_filter = ('report_type', 'farm')
    # Barre de recherche sur la ferme et le type de rapport
    search_fields = ('farm__name', 'report_type')

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    # Affiche les champs 'productor' et 'last_updated' dans la liste d'affichage
    list_display = ('productor', 'last_updated')
    # Ajoute un filtre pour la ferme associée
    list_filter = ('productor__farm_name',)
    # Barre de recherche sur le nom de la ferme du producteur
    search_fields = ('productor__farm_name',)

