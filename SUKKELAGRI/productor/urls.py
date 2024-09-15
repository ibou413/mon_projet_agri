from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import FarmViewSet, ProductorProfileViewSet, CropViewSet, SensorViewSet, SensorDataViewSet, DataAnalysisViewSet, StatisticalReportViewSet, DashboardViewSet

router = DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'productor-profiles', ProductorProfileViewSet)
router.register(r'crops', CropViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'sensor-data', SensorDataViewSet)
router.register(r'data-analyses', DataAnalysisViewSet)
router.register(r'statistical-reports', StatisticalReportViewSet)
router.register(r'dashboards', DashboardViewSet)


app_name = 'productor'

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('no_farm/', views.nofarm, name='no_farm'),
    path('add_crop/', views.add_crop, name='add_crop'),
    path('weather_forecasts/', views.weather_forecasts, name='weather_forecasts'),
]
