from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Crop

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'user_type', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

# productor/forms.py



class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'description', 'planting_season', 'harvest_time']  # Ajuste les champs selon ton modèle

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['planting_season'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['harvest_time'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
