from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'productor/home.html')


@login_required
def nofarm(request):
    return render(request, 'productor/no_farm.html')

# productor/views.py

from django.shortcuts import render
from .models import Farm, Sensor, SensorData, WeatherForecast
@login_required
def dashboard(request):
    user = request.user
    try:
        # Assumes one farm per user. If multiple farms are possible, you'll need to handle that.
        farm = Farm.objects.get(owner=user)
    except Farm.DoesNotExist:
        # Handle case where the user does not have a farm (you can redirect or show a message)
        return render(request, 'productor/no_farm.html')

    # Retrieve all sensors for this farm
    sensors = Sensor.objects.filter(farm=farm)
    
    # Get sensor data related to these sensors
    sensor_data = SensorData.objects.filter(sensor__in=sensors)
    
    # Get weather forecasts for this farm
    weather_forecasts = WeatherForecast.objects.filter(farm=farm)
    
    # If you want to calculate specific statistics, uncomment and update
    # Example: Calculate average temperature from sensor data if relevant
    # average_temperature = sensor_data.filter(sensor__type='temperature').aggregate(
    #     avg_temp=models.Avg('data__temperature'))['avg_temp']

    context = {
        'farm': farm,
        'sensors': sensors,
        'sensor_data': sensor_data,
        'weather_forecasts': weather_forecasts,
        # 'average_temperature': average_temperature,  # Add if needed
    }

    return render(request, 'productor/dashboard.html', context)

from django.shortcuts import render, redirect
from .forms import CropForm

@login_required
def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productor:home')
    else:
        form = CropForm()
    
    return render(request, 'productor/add_crop.html', {'form': form})


# productor/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productor.models import Farm, WeatherForecast

@login_required
def weather_forecasts(request):
    user = request.user
    try:
        farm = Farm.objects.get(owner=user)
        forecasts = WeatherForecast.objects.filter(farm=farm)
    except Farm.DoesNotExist:
        # Redirige vers une page où l'utilisateur peut créer une ferme
        return redirect('productor:no_farm')  # Assurez-vous que 'no_farm' est une URL valide dans vos urls.py

    context = {
        'forecasts': forecasts,
    }
    return render(request, 'productor/weather_forecasts.html', context)

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('home')  # Page d'accueil de l'application principale

from rest_framework import generics
from .models import CustomUser, Farm, WeatherForecast
from .serializers import CustomUserSerializer, FarmSerializer, WeatherForecastSerializer

# Vues pour CustomUser
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# Vues pour Farm
class FarmListCreateAPIView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

# Vues pour WeatherForecast
class WeatherForecastListCreateAPIView(generics.ListCreateAPIView):
    queryset = WeatherForecast.objects.all()
    serializer_class = WeatherForecastSerializer
