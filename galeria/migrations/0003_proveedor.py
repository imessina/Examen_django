# Generated by Django 5.0.6 on 2024-07-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_tipoproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('razon_social', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('tipo_pago', models.CharField(choices=[('CR', 'Crédito'), ('CO', 'Contado')], max_length=2)),
            ],
        ),
    ]
