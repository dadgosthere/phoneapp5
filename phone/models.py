from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Sepet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kullanıcıya bağlı olarak sepete eklemek istiyorsanız
    product_id = models.IntegerField()  # Sepete eklenen ürünün kimliği
    added_at = models.DateTimeField(auto_now_add=True)

class apple(models.Model):
    apple_name = models.CharField(max_length=100, verbose_name="Ürün adı")
    apple_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün fiyatı")
    apple_description = RichTextField(verbose_name="Ürün açıklaması")
    apple_image = models.ImageField(upload_to='apple/', verbose_name="Ürün resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")

    def __str__(self):
        return self.apple_name


class samsung(models.Model):
    samsung_name = models.CharField(max_length=100, verbose_name="ürün adı")
    samsung_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    samsung_description = models.TextField(verbose_name="Ürün Açıklaması")
    samsung_image = models.ImageField(upload_to='samsung/', verbose_name="Ürün Resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")
    

    def __str__(self):
        return self.samsung_name


class xiaomi(models.Model):
    xiaomi_name = models.CharField(max_length=100, verbose_name="ürün adı")
    xiaomi_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    xiaomi_description = models.TextField(verbose_name="Ürün Açıklaması")
    xiaomi_image = models.ImageField(upload_to='xiaomi/', verbose_name="Ürün Resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")
    

    def __str__(self):
        return self.xiaomi_name


class oppo(models.Model):
    oppo_name = models.CharField(max_length=100, verbose_name="ürün adı")
    oppo_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    oppo_description = models.TextField(verbose_name="Ürün Açıklaması")
    oppo_image = models.ImageField(upload_to='oppo/', verbose_name="Ürün Resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")

    def __str__(self):
        return self.oppo_name


class realme(models.Model):
    realme_name = models.CharField(max_length=100, verbose_name="ürün adı")
    realme_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    realme_description = models.TextField(verbose_name="Ürün Açıklaması")
    realme_image = models.ImageField(upload_to='realme/', verbose_name="Ürün Resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")
    
    def __str__(self):
        return self.realme_name


class huawei(models.Model):
    huawei_name = models.CharField(max_length=100, verbose_name="ürün adı")
    huawei_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    huawei_description = models.TextField(verbose_name="Ürün Açıklaması")
    huawei_image = models.ImageField(upload_to='huawei/', verbose_name="Ürün Resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")

    def __str__(self):
        return self.huawei_name


class macbook(models.Model):
    macbook_name = models.CharField(max_length=100, verbose_name="ürün adı")
    macbook_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    macbook_description = models.TextField(verbose_name="Ürün Açıklaması")
    macbook_image = models.ImageField(upload_to='macbook/', verbose_name="Ürün Resmi")
    internal_memory = models.CharField(max_length=50, verbose_name="Dahili hafıza", default="Bilinmiyor")
    screen_size_range = models.CharField(max_length=50, verbose_name="Ekran boyut aralığı", default="Bilinmiyor")
    camera_resolution_range = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü aralığı", default="Bilinmiyor")
    screen_size = models.CharField(max_length=50, verbose_name="Ekran boyutu", default="Bilinmiyor")
    warranty_type = models.CharField(max_length=100, verbose_name="Garanti tipi", default="Bilinmiyor")
    wireless_charging = models.BooleanField(default=False, verbose_name="Kablosuz şarj")
    camera_resolution = models.CharField(max_length=50, verbose_name="Kamera çözünürlüğü", default="Bilinmiyor")
    front_camera = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera", default="Bilinmiyor")
    battery_capacity = models.CharField(max_length=50, verbose_name="Pil gücü", default="Bilinmiyor")
    ram_capacity = models.CharField(max_length=50, verbose_name="RAM kapasitesi", default="Bilinmiyor")
    face_recognition = models.BooleanField(default=False, verbose_name="Yüz tanıma")
    front_camera_range = models.CharField(max_length=50, verbose_name="Ön (Selfie) kamera aralığı", default="Bilinmiyor")
    battery_capacity_range = models.CharField(max_length=50, verbose_name="Pil gücü aralığı", default="Bilinmiyor")

    def __str__(self):
        return self.macbook_name


class other(models.Model):
    other_name = models.CharField(max_length=100, verbose_name="ürün adı")
    other_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    other_description = models.TextField(verbose_name="Ürün Açıklaması")
    other_image = models.ImageField(upload_to='other/', verbose_name="Ürün Resmi")

    def __str__(self):
        return self.other_name


class kulaklik(models.Model):
    kulaklik_name = models.CharField(max_length=100, verbose_name="ürün adı")
    kulaklik_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ürün Fiyatı")
    kulaklik_description = models.TextField(verbose_name="Ürün Açıklaması")
    kulaklik_image = models.ImageField(upload_to='kulaklik/', verbose_name="Ürün Resmi")

    def __str__(self):
        return self.kulaklik_name
    


class CekilisKodu(models.Model):
    kod = models.CharField(max_length=20, unique=True)
    kullanildi_mi = models.BooleanField(default=False)

    def __str__(self):
        return self.kod