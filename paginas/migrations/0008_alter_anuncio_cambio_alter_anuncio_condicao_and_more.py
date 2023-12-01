# Generated by Django 4.2.7 on 2023-12-01 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0007_alter_anuncio_cambio_alter_anuncio_condicao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='cambio',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatico', 'Automatico')], default='Manual', max_length=20),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='condicao',
            field=models.CharField(choices=[('Novos', 'Novo'), ('SemiNovos', 'Semi Novo'), ('Usados', 'Usado')], default='Novos', max_length=20),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='marca',
            field=models.CharField(choices=[('Tesla', 'Tesla'), ('Nenhuma_dessas_marca', 'Nenhuma dessas'), ('Volkswagen', 'Volkswagen'), ('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Lamborghini', 'Lamborghini'), ('Porsche', 'Porsche'), ('Ferrari', 'Ferrari'), ('Peugeot', 'Peugeot')], default='Nenhuma_dessas_marca', max_length=20),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='Partida',
            field=models.CharField(choices=[('elétrica', 'Elétrica'), ('pedal', 'Pedal')], default='Pedal', max_length=30),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='condicao',
            field=models.CharField(choices=[('Novos', 'Novo'), ('SemiNovos', 'Semi Novo'), ('Usados', 'Usado')], default='Novos', max_length=20),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='marca',
            field=models.CharField(choices=[('Kawasaki', 'Kawasaki'), ('Honda', 'Honda'), ('BMW', 'BMW'), ('Nenhuma_dessas_marca', 'Nenhuma dessas'), ('Bimota', 'Bimota'), ('Ducati', 'Ducati'), ('Suzuki', 'Suzuki'), ('Dafra', 'Dafra'), ('Yamaha', 'Yamaha')], default='Nenhuma_dessas_marca', max_length=20),
        ),
        migrations.AlterField(
            model_name='anunciomoto',
            name='precoo',
            field=models.CharField(choices=[('LowToHigh', 'Abaixo de 30k'), ('HighToLow', 'Acima de 30k')], default='Abaixo de 30k', max_length=20),
        ),
    ]
