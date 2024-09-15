from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('farms/', views.FarmListCreateAPIView.as_view(), name='farm-list-create'),
    path('weather-forecasts/', views.WeatherForecastListCreateAPIView.as_view(), name='weather-forecast-list-create'),
    # Ajoutez d'autres routes API ici
]
