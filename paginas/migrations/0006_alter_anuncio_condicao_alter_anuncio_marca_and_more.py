# Generated by Django 4.2.7 on 2023-12-01 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_alter_anuncio_cambio_alter_anuncio_condicao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='condicao',
            field=models.CharField(choices=[('Novos', 'Novo'), ('Usados', 'Usado'), ('SemiNovos', 'Semi Novo')], default='Novos', max_length=20),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='marca',
            field=models.CharField(choices=[('Ferrari', 'Ferrari'), ('Tesla', 'Tesla'), ('Porsche', 'Porsche'), ('Lamborghini', 'Lamborghini'), ('Nenhuma_dessas_marca', 'Nenhuma dessas'), ('Peugeot', 'Peugeot'), ('Ford', 'Ford'), ('Volkswagen', 'Volkswagen'), ('Chevrolet', 'Chevrolet')], default='Nenhuma_dessas_marca', max_length=20),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='precoo',
            field=models.CharField(choices=[('HighToLow', 'Acima de 100k'), ('LowToHigh', 'Abaixo de 100k')], default='Abaixo de 100k', max_length=20),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='Partida',
            field=models.CharField(choices=[('elétrica', 'Elétrica'), ('pedal', 'Pedal')], default='Pedal', max_length=30),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='condicao',
            field=models.CharField(choices=[('Novos', 'Novo'), ('Usados', 'Usado'), ('SemiNovos', 'Semi Novo')], default='Novos', max_length=20),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='marca',
            field=models.CharField(choices=[('Ducati', 'Ducati'), ('Bimota', 'Bimota'), ('BMW', 'BMW'), ('Honda', 'Honda'), ('Suzuki', 'Suzuki'), ('Kawasaki', 'Kawasaki'), ('Dafra', 'Dafra'), ('Nenhuma_dessas_marca', 'Nenhuma dessas'), ('Yamaha', 'Yamaha')], default='Nenhuma_dessas_marca', max_length=20),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='precoo',
            field=models.CharField(choices=[('LowToHigh', 'Abaixo de 30k'), ('HighToLow', 'Acima de 30k')], default='Abaixo de 30k', max_length=20),
        ),
    ]
