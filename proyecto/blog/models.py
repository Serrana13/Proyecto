from django.db import models

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):

    titulo = models.CharField(max_length=200)

    subtitulo = models.CharField(max_length=200)

    contenido = RichTextField()

    imagen = models.ImageField(upload_to='posts', null=True, blank=True)

    fecha = models.DateField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        
        return self.titulo