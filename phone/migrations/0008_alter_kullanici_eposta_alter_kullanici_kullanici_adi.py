# Generated by Django 5.0.2 on 2024-02-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0007_kullanici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanici',
            name='eposta',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='kullanici',
            name='kullanici_adi',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
