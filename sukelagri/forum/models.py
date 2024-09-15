# forum/models.py

from django.db import models
from django.conf import settings

# Modèle représentant un post dans le forum
class Post(models.Model):
    # Référence à l'auteur du post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Titre du post
    title = models.CharField(max_length=255)
    # Contenu du post
    content = models.TextField()
    # Date de création du post
    created_at = models.DateTimeField(auto_now_add=True)
    # Date de la dernière mise à jour du post
    updated_at = models.DateTimeField(auto_now=True)
    # Autres champs pertinents

    def __str__(self):
        return self.title

# Modèle représentant un commentaire sur un post
class Comment(models.Model):
    # Référence au post auquel le commentaire est associé
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    # Référence à l'auteur du commentaire
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Contenu du commentaire
    content = models.TextField()
    # Date de création du commentaire
    created_at = models.DateTimeField(auto_now_add=True)
    # Autres champs pertinents

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

# Modèle représentant une catégorie de forum
class Category(models.Model):
    # Nom de la catégorie
    name = models.CharField(max_length=100)
    # Description de la catégorie
    description = models.TextField()
    # Autres champs pertinents

    def __str__(self):
        return self.name
