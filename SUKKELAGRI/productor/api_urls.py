from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CustomUserViewset, WeatherForecastViewSet, FarmViewSet, CropViewSet, SensorViewSet, SensorDataViewSet, ProductorProfileViewSet, DataAnalysisViewSet, StatisticalReportViewSet, DashboardViewSet 
router = DefaultRouter()

# Enregistrement des ViewSets dans le routeur
router.register(r'users', CustomUserViewset)
router.register(r'farms', FarmViewSet)
router.register(r'productors', ProductorProfileViewSet)
router.register(r'crops', CropViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'sensor-data', SensorDataViewSet)
router.register(r'data-analysis', DataAnalysisViewSet)
router.register(r'statistical-reports', StatisticalReportViewSet)
router.register(r'dashboards', DashboardViewSet)
router.register(r'weather-forecasts', WeatherForecastViewSet)  # Nouvelle route pour WeatherForecast


urlpatterns = [
    path('', include(router.urls)),
]
