# Generated by Django 4.2.2 on 2023-07-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(to='Menu.categoria'),
        ),
    ]
