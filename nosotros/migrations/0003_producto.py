# Generated by Django 4.2.2 on 2023-07-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0002_contacto_galeria_quienes_somos_delete_pedidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripción', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
