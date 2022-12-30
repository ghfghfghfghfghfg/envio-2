from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  
from ckeditor_uploader.fields import RichTextUploadingField  
from django.contrib.auth.models import User
from django.db.models import Func, IntegerField
# Create your models here.


# blog model's
class Post(models.Model):
    titulo =models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateField(auto_now_add=True)
   
    #miniatura_img = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.titulo


LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

ATIVIDADE=[
    ('sedentario','sedentario'),
    ('levemente ativo','levemente ativo'),
    ('moderadamente','moderadamente'),
    ('muito ativo','muito ativo'),
    ('extremamente','extremamente'),

]

class Perfil(models.Model):
    genero = models.CharField(max_length=150,choices=LISTA_SEXO,default='Masculino',null=True)
    idade = models.IntegerField(null=True)
    peso = models.IntegerField(null=True)
    altura = models.CharField(max_length=3,null=True)
    atividade_fisica = models.CharField(max_length=150,choices=ATIVIDADE,default='Feminino',null=True)
    #imc = (float(idade)-float(peso))


    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

