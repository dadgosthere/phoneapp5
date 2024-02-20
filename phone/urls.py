from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("hesap/", views.hesap, name="hesap"),
    path("cekilis/", views.cekilis, name="cekilis"),
    path('apple/<int:apple_id>/', views.apple_detay, name='apple_detay'),
    path('apple/', views.apple_view, name='apple'),
    path('sepet/', views.sepet, name='sepet'),
    path('samsung/', views.samsung_view, name='samsung'),
    path('samsung_detay/<int:samsung_id>/', views.samsung_detay, name='samsung_detay'),

    path('xiaomi/', views.xiaomi_view, name='xiaomi'),
    path('xiaomi_detay/<int:xiaomi_id>/', views.xiaomi_detay, name='xiaomi_detay'),

    path('oppo/', views.oppo_view, name='oppo'),
    path('oppo_detay/<int:oppo_id>/', views.oppo_detay, name='oppo_detay'),

    path('realme/', views.realme_view, name='realme'),
    path('realme_detay/<int:realme_id>/', views.realme_detay, name='realme_detay'),

    path('huawei/', views.huawei_view, name='huawei'),
    path('huawei_detay/<int:huawei_id>/', views.huawei_detay, name='huawei_detay'),

    path('macbook/', views.macbook_view, name='macbook'),
    path('macbook_detay/<int:macbook_id>/', views.macbook_detay, name='macbook_detay'),

    path('kulaklik/', views.kulaklik_view, name='kulaklik'),
    path('kulaklik_detay/<int:kulaklik_id>/', views.kulaklik_detay, name='kulaklik_detay'),

    path('other/', views.other_view, name='other'),
    path('other_detay/<int:other_id>/', views.other_detay, name='other_detay'),

    path('teslimat/', views.teslimat, name='teslimat'),
    path('gizlilik/', views.gizlilik, name='gizlilik'),
    path('kullanım/', views.kullanım, name='kullanım'),
    path('iade/', views.iade, name='iade'),
    path('Iletisim/', views.Iletisim, name='Iletisim'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
