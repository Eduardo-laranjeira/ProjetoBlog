from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=500)
    texto = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    imagem = models.ImageField(upload_to = 'uploads/', default="")

class Comentario(models.Model):
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    comentario_text = models.CharField(max_length=200)
    com_date = models.DateTimeField('date published')