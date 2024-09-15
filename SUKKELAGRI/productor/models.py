from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Gestionnaire personnalisé pour le modèle utilisateur
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)  # Normalise l'email
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)  # Hash le mot de passe
        user.save(using=self._db)  # Sauvegarde l'utilisateur dans la base de données
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Définit l'utilisateur comme membre du staff
        extra_fields.setdefault('is_superuser', True)  # Définit l'utilisateur comme super utilisateur
        return self.create_user(email, first_name, last_name, password, **extra_fields)

# Modèle utilisateur personnalisé
class CustomUser(AbstractBaseUser):
    USER_TYPE_CHOICES = [
        ('producer', 'Producer'),
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    ]
    email = models.EmailField(unique=True)  # Champ unique pour l'email
    first_name = models.CharField(max_length=30)  # Prénom de l'utilisateur
    last_name = models.CharField(max_length=30)  # Nom de famille de l'utilisateur
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)  # Type d'utilisateur
    is_active = models.BooleanField(default=True)  # Indique si l'utilisateur est actif
    is_staff = models.BooleanField(default=False)  # Indique si l'utilisateur est membre du staff

    objects = CustomUserManager()  # Attribue le gestionnaire personnalisé

    USERNAME_FIELD = 'email'  # Utilise l'email comme identifiant pour l'authentification
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Champs requis lors de la création d'un utilisateur


# Modèle pour une ferme
class Farm(models.Model):
    name = models.CharField(max_length=255)  # Nom de la ferme
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Propriétaire de la ferme (référence au modèle CustomUser)
    location = models.CharField(max_length=255)  # Localisation de la ferme


# Modèle pour les prévisions météorologiques
class WeatherForecast(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)  # Ferme pour laquelle la prévision est faite (référence au modèle Farm)
    forecast_date = models.DateField()  # Date de la prévision
    forecast_data = models.JSONField()  # Données de la prévision sous forme de JSON



from django.db import models
from django.conf import settings

# Profil du producteur associé à un utilisateur
class ProductorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Le nom de la ferme du producteur
    farm_name = models.CharField(max_length=255)
    # Localisation de la ferme
    location = models.CharField(max_length=255)
    # Numéro de contact du producteur
    contact_number = models.CharField(max_length=20)
    # Autres champs pertinents

    def __str__(self):
        return self.farm_name

# Modèle représentant les cultures
class Crop(models.Model):
    # Nom de la culture
    name = models.CharField(max_length=255)
    # Description de la culture
    description = models.TextField()
    # Saison de plantation de la culture
    planting_season = models.CharField(max_length=100)
    # Temps de récolte de la culture
    harvest_time = models.CharField(max_length=100)
    # Autres champs pertinents

    def __str__(self):
        return self.name

# Modèle représentant un capteur sur une ferme
class Sensor(models.Model):
    # Référence à la ferme où le capteur est installé
    farm = models.ForeignKey('ProductorProfile', on_delete=models.CASCADE)
    # Type de capteur (température, humidité, etc.)
    type = models.CharField(max_length=100)
    # Emplacement du capteur sur la ferme
    location = models.CharField(max_length=255)
    # Date d'installation du capteur
    installation_date = models.DateField()
    # Autres champs pertinents

    def __str__(self):
        return f"{self.type} - {self.location}"

# Modèle représentant les données collectées par un capteur
class SensorData(models.Model):
    # Référence au capteur qui a collecté les données
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    # Date et heure de la collecte des données
    timestamp = models.DateTimeField()
    # Données collectées au format JSON
    data = models.JSONField()  # Stocke les données sous forme de JSON

    def __str__(self):
        return f"{self.sensor} - {self.timestamp}"
    
from django.db import models
from django.conf import settings

# Modèle représentant une analyse de données
class DataAnalysis(models.Model):
    # Référence à la ferme pour laquelle l'analyse est effectuée
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    # Type d'analyse (par exemple, analyse de la température, de l'humidité, etc.)
    analysis_type = models.CharField(max_length=100)
    # Résultats de l'analyse sous forme de JSON
    result_data = models.JSONField()
    # Date et heure de l'analyse
    analysis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.analysis_type} analysis for {self.farm.name} on {self.analysis_date}"

# Modèle représentant un rapport statistique
class StatisticalReport(models.Model):
    # Référence à la ferme pour laquelle le rapport est généré
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    # Type de rapport (par exemple, rapport de rendement, rapport climatique, etc.)
    report_type = models.CharField(max_length=100)
    # Données statistiques sous forme de JSON
    statistics = models.JSONField()
    # Date de création du rapport
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} report for {self.farm.name} on {self.report_date}"

# Modèle représentant un tableau de bord pour un producteur
class Dashboard(models.Model):
    # Référence au producteur pour lequel le tableau de bord est créé
    productor = models.OneToOneField('ProductorProfile', on_delete=models.CASCADE)
    # Données du tableau de bord sous forme de JSON
    dashboard_data = models.JSONField()
    # Date de la dernière mise à jour du tableau de bord
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dashboard for {self.productor.farm_name}"
