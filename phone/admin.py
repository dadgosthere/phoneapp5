from django.contrib import admin
from .models import apple, xiaomi, oppo, huawei, other, kulaklik, macbook, realme, samsung, CekilisKodu,Sepet
# Register your models here.


class appleadmin(admin.ModelAdmin):
    list_display = ('apple_name', 'apple_description')  # Listede görünecek sütunları belirtin



admin.site.register(apple,appleadmin)
admin.site.register(xiaomi)
admin.site.register(oppo)
admin.site.register(huawei)
admin.site.register(other)
admin.site.register(kulaklik)
admin.site.register(macbook)
admin.site.register(realme)
admin.site.register(samsung)
admin.site.register(CekilisKodu)
admin.site.register(Sepet)


