from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomLogoutView, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    
    # Routes vers les applications spécifiques
    path('productor/', include('productor.urls', namespace='productor')),
    path('market/', include('market.urls', namespace='market')),
    path('forum/', include('forum.urls', namespace='forum')),
    
    # Routes d'authentification
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Routes pour la gestion des mots de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Routes API
    path('api/productor/', include('productor.api_urls')),  # Assurez-vous que 'api_urls' existe dans l'application productor
    path('api/market/', include('market.api_urls')),        # Assurez-vous que 'api_urls' existe dans l'application market
    path('api/forum/', include('forum.api_urls')),          # Assurez-vous que 'api_urls' existe dans l'application forum
]
