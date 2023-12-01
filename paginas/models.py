from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Anuncio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    carro = models.ImageField(default='avatar.png', upload_to='midia', verbose_name='Imagem do carro')
    modelo = models.CharField(max_length=40, verbose_name='Modelo do carro')
    mar = {
        ("Ford", "Ford"),
        ("Peugeot", "Peugeot"),
        ("Tesla", "Tesla"),
        ("Chevrolet", "Chevrolet"),
        ("Porsche", "Porsche"),
        ("Lamborghini", "Lamborghini"),
        ("Volkswagen", "Volkswagen"),
        ("Ferrari", "Ferrari"),
        ("Nenhuma_dessas_marca", "Nenhuma dessas"),
    }

    marca = models.CharField(max_length=20, choices=mar, default="Nenhuma_dessas_marca")

    condi = {
        ("Usados", "Usado"),
        ("SemiNovos", "Semi Novo"),
        ("Novos", "Novo"),
    }

    condicao = models.CharField(max_length=20, choices=condi, default="Novos")

    ip = {
        ("Sim", "Sim"),
        ("Não", "Não"),
    }

    cambi = {
        ("Automatico", "Automatico"),
        ("Manual", "Manual"),
    }

    tro = {
        ("Sim", "Sim"),
        ("Não", "Não"),
    }

    pre = {
        ("LowToHigh", "Abaixo de 100k"),
        ("HighToLow", "Acima de 100k"),
    }

    precoo = models.CharField(max_length=20, choices=pre, default="Abaixo de 100k")

    descricao = models.CharField(max_length=1000, verbose_name='Descrição do carro')
    preco = models.CharField(max_length=20, verbose_name='Preço do carro')
    data = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    km = models.CharField(max_length=100,verbose_name='Quilometros')
    troca = models.CharField(max_length=10,choices=tro, default='Não', verbose_name='Aceita Troca')
    combustivel = models.CharField(max_length=30)
    cambio = models.CharField(max_length=20, choices=cambi, default="Manual")
    cor = models.CharField(max_length=20)
    ipva = models.CharField(max_length=10, choices=ip, default="Sim")

    def __str__(self):
        return f'{self.usuario.username}-Anuncio'
    

    
class AnuncioMoto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    moto = models.ImageField(default='avatar.png', upload_to='midia', verbose_name='Imagem da moto')
    modelo = models.CharField(max_length=40, verbose_name='Modelo da moto')

    mar = {
        ("Dafra", "Dafra"),
        ("BMW", "BMW"),
        ("Kawasaki", "Kawasaki"),
        ("Suzuki", "Suzuki"),
        ("Honda", "Honda"),
        ("Yamaha", "Yamaha"),
        ("Ducati", "Ducati"),
        ("Bimota", "Bimota"),
        ("Nenhuma_dessas_marca", "Nenhuma dessas"),
    }

    marca = models.CharField(max_length=20, choices=mar, default="Nenhuma_dessas_marca")

    condi = {
        ("Usados", "Usado"),
        ("SemiNovos", "Semi Novo"),
        ("Novos", "Novo"),
    }

    condicao = models.CharField(max_length=20, choices=condi, default="Novos")

    pre = {
        ("LowToHigh", "Abaixo de 30k"),
        ("HighToLow", "Acima de 30k"),
    }

    ip = {
        ("Sim", "Sim"),
        ("Não", "Não"),
    }

    cambi = {
        ("líquido", "líquido"),
        ("ar", "Ar"),
    }

    tro = {
        ("Sim", "Sim"),
        ("Não", "Não"),
    }

    parti = {
        ("pedal", "Pedal"),
        ("elétrica", "Elétrica"),
    }

    precoo = models.CharField(max_length=20, choices=pre, default="Abaixo de 30k")
    descricao = models.CharField(max_length=1000, verbose_name='Descrição da moto')
    preco = models.CharField(max_length=20,verbose_name='Preço do carro')
    data = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    km = models.CharField(max_length=100,verbose_name='Quilometros')
    troca = models.CharField(max_length=10,choices=tro, default='Não', verbose_name='Aceita Troca')
    Refrigeracao = models.CharField(max_length=20, choices=cambi, default="Líquido", verbose_name='Refrigeração')
    cor = models.CharField(max_length=20)
    ipva = models.CharField(max_length=10, choices=ip, default="Sim")
    Partida = models.CharField(max_length=30, choices=parti, default='Pedal')
    Cilindrada = models.IntegerField()
    marchas = models.IntegerField()


    def __str__(self):
        return f'{self.usuario.username}-Anuncio-moto'