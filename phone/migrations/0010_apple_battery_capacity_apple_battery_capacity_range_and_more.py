# Generated by Django 5.0.2 on 2024-02-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0009_delete_kullanici'),
    ]

    operations = [
        migrations.AddField(
            model_name='apple',
            name='battery_capacity',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Pil gücü'),
        ),
        migrations.AddField(
            model_name='apple',
            name='battery_capacity_range',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Pil gücü aralığı'),
        ),
        migrations.AddField(
            model_name='apple',
            name='camera_resolution',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Kamera çözünürlüğü'),
        ),
        migrations.AddField(
            model_name='apple',
            name='camera_resolution_range',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Kamera çözünürlüğü aralığı'),
        ),
        migrations.AddField(
            model_name='apple',
            name='face_recognition',
            field=models.BooleanField(default=False, verbose_name='Yüz tanıma'),
        ),
        migrations.AddField(
            model_name='apple',
            name='front_camera',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Ön (Selfie) kamera'),
        ),
        migrations.AddField(
            model_name='apple',
            name='front_camera_range',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Ön (Selfie) kamera aralığı'),
        ),
        migrations.AddField(
            model_name='apple',
            name='internal_memory',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Dahili hafıza'),
        ),
        migrations.AddField(
            model_name='apple',
            name='ram_capacity',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='RAM kapasitesi'),
        ),
        migrations.AddField(
            model_name='apple',
            name='screen_size',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Ekran boyutu'),
        ),
        migrations.AddField(
            model_name='apple',
            name='screen_size_range',
            field=models.CharField(default='Bilinmiyor', max_length=50, verbose_name='Ekran boyut aralığı'),
        ),
        migrations.AddField(
            model_name='apple',
            name='warranty_type',
            field=models.CharField(default='Bilinmiyor', max_length=100, verbose_name='Garanti tipi'),
        ),
        migrations.AddField(
            model_name='apple',
            name='wireless_charging',
            field=models.BooleanField(default=False, verbose_name='Kablosuz şarj'),
        ),
        migrations.AlterField(
            model_name='apple',
            name='apple_description',
            field=models.TextField(verbose_name='Ürün açıklaması'),
        ),
        migrations.AlterField(
            model_name='apple',
            name='apple_image',
            field=models.ImageField(upload_to='apple/', verbose_name='Ürün resmi'),
        ),
        migrations.AlterField(
            model_name='apple',
            name='apple_name',
            field=models.CharField(max_length=100, verbose_name='Ürün adı'),
        ),
        migrations.AlterField(
            model_name='apple',
            name='apple_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ürün fiyatı'),
        ),
    ]
