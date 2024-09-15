from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from productor.forms import CustomUserCreationForm, CustomAuthenticationForm  # Assurez-vous de créer ces formulaires dans l'application Productor


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')


class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        
        # Vérifie le type d'utilisateur pour la redirection
        if user.user_type == 'producer':
            return reverse_lazy('productor:home')  # Redirection vers l'application Productor
        elif user.user_type == 'seller':
            return reverse_lazy('market:home')  # Redirection vers l'application Market
        elif user.user_type == 'buyer':
            return reverse_lazy('market:home')  # Redirection pour les acheteurs (peut-être vers une page spécifique aux acheteurs ou une autre application)
        else:
            return reverse_lazy('home')  # Redirection par défaut en cas de type d'utilisateur inconnu

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
   # template_name = 'registration/logout.html'  # Assurez-vous que ce template existe

    def get_next_page(self):
        user = self.request.user
        if user.is_authenticated:
            if user.user_type == 'producer':
                return reverse_lazy('productor:home')
            elif user.user_type in ['seller', 'buyer']:
                return reverse_lazy('market:home')
        return reverse_lazy('home')



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
           # login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
