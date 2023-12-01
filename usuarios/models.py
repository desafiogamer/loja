from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagemPerfil = models.ImageField(default='avatar.png', upload_to='midia', verbose_name='Imagem do perfil')
    dataa = models.DateField(null=True, verbose_name='Data de nascimento')
    cep = models.CharField(max_length=10, null=True, verbose_name='CEP')
    estado = models.CharField(max_length=40, null=True)
    cidade = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=15, null=True, verbose_name='CPF')
    nome = models.CharField(max_length=50, null=True, verbose_name='Nome completo')
    telefone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.usuario.username}-Profile'