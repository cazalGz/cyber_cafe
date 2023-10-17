# Generated by Django 4.2.2 on 2023-08-31 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0005_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripción', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='Menu')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ManyToManyField(to='Menu.categoria')),
            ],
        ),
    ]
