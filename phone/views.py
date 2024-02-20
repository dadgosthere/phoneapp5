from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
import os
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from .models import apple, xiaomi, oppo, huawei, other, kulaklik, macbook, realme,samsung, CekilisKodu,Sepet
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from random import sample


# Create your views here.


def index(request):
    all_apples = apple.objects.all()
    random_apples = sample(list(all_apples), min(len(all_apples), 5))

    all_xiaomis = xiaomi.objects.all()
    random_xiaomis = sample(list(all_xiaomis), min(len(all_xiaomis), 5))

    all_oppo = oppo.objects.all()
    random_oppo = sample(list(all_oppo), min(len(all_oppo), 5))

    all_other = other.objects.all()
    random_other = sample(list(all_other), min(len(all_other), 5))

    all_huawei = huawei.objects.all()
    random_huawei = sample(list(all_huawei), min(len(all_huawei), 5))

    all_kulaklik = kulaklik.objects.all()
    random_kulaklik = sample(list(all_kulaklik), min(len(all_kulaklik), 5))

    all_macbook = macbook.objects.all()
    random_macbook = sample(list(all_macbook), min(len(all_macbook), 5))

    all_realme = realme.objects.all()
    random_realme = sample(list(all_realme), min(len(all_realme), 5))

    all_samsung = samsung.objects.all()
    random_samsung = sample(list(all_samsung), min(len(all_samsung), 5))

    media_url = os.path.join('/', 'media')

    return render(request, "index.html", {'all_apples': all_apples, 'random_apples': random_apples, 
                                          'all_xiaomis': all_xiaomis, 'random_xiaomis': random_xiaomis, 
                                          'all_oppo': all_oppo, 'random_oppo': random_oppo,
                                          'all_other': all_other, 'random_other': random_other,
                                          'all_huawei': all_huawei, 'random_huawei': random_huawei,
                                          'all_kulaklik': all_kulaklik, 'random_kulaklik': random_kulaklik,
                                          'all_macbook': all_macbook, 'random_macbook': random_macbook,
                                          'all_realme': all_realme, 'random_realme': random_realme,
                                          'all_samsung': all_samsung, 'random_samsung': random_samsung,
                                          'media_url': media_url})

# def index(request):
#     all_apples = apple.objects.all()
#     random_apples = sample(list(all_apples), 10)
#     apple2 = apple.objects.all()
#     xiaomi2 = xiaomi.objects.all()
#     oppo2 = oppo.objects.all()
#     other2 = other.objects.all()
#     huawei2 = huawei.objects.all()
#     kulaklik2 = kulaklik.objects.all()
#     macbook2 = macbook.objects.all()
#     realme2 = realme.objects.all()
#     samsung2 = samsung.objects.all()
#     media_url2 = os.path.join('/', 'media')
#     return render(request, "index.html", {'all_apples': all_apples, 'random_apples': random_apples, 'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})


def hesap(request):
    if not request.user.is_authenticated:
        return redirect("home")
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "hesap.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

# def cekilis(request):

#     return render(request, "cekilis.html")

def cekilis(request):
    message = None
    message2 = None
    if request.method == 'POST':
        kod = request.POST.get('kod')
        try:
            cekilis_kodu = CekilisKodu.objects.get(kod=kod)
            if not cekilis_kodu.kullanildi_mi:
                cekilis_kodu.kullanildi_mi = True
                cekilis_kodu.save()
                message2 = "Kazandınız! Ödülünüzü almak için bizimle iletişime geçiniz."
            else:
                message = "Bu kod daha önce kullanılmış."
        except CekilisKodu.DoesNotExist:
            message = "Geçersiz kod."

        return render(request, 'cekilis.html', {'message': message, 'message2': message2})

    return render(request, 'cekilis.html')


def apple_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "apple.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def apple_detay(request, apple_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    apple_obj = get_object_or_404(apple, pk=apple_id)
    return render(request, 'apple_detay.html', {'apple': apple_obj, 'apple2':apple2})


def sepet(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "sepet.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})


def samsung_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "samsung.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def samsung_detay(request, samsung_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    samsung_obj = get_object_or_404(samsung, pk=samsung_id)
    return render(request, 'samsung_detay.html', {'samsung': samsung_obj, 'samsung2':samsung2})

def xiaomi_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "xiaomi.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def xiaomi_detay(request, xiaomi_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    xiaomi_obj = get_object_or_404(xiaomi, pk=xiaomi_id)
    return render(request, 'xiaomi_detay.html', {'xiaomi': xiaomi_obj, 'xiaomi2':xiaomi2})

def oppo_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "oppo.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def oppo_detay(request, oppo_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    oppo_obj = get_object_or_404(oppo, pk=oppo_id)
    return render(request, 'oppo_detay.html', {'oppo': oppo_obj, 'oppo2':oppo2})

def realme_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "realme.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def realme_detay(request, realme_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    realme_obj = get_object_or_404(realme, pk=realme_id)
    return render(request, 'realme_detay.html', {'realme': realme_obj, 'realme2':realme2})

def huawei_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "huawei.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def huawei_detay(request, huawei_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    huawei_obj = get_object_or_404(huawei, pk=huawei_id)
    return render(request, 'huawei_detay.html', {'huawei': huawei_obj, 'huawei2':huawei2})

def macbook_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "macbook.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def macbook_detay(request, macbook_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    macbook_obj = get_object_or_404(macbook, pk=macbook_id)
    return render(request, 'macbook_detay.html', {'macbook': macbook_obj, 'macbook2':macbook2})

def kulaklik_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "kulaklık.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def kulaklik_detay(request, kulaklik_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    kulaklik_obj = get_object_or_404(kulaklik, pk=kulaklik_id)
    return render(request, 'kulaklık_detay.html', {'kulaklik': kulaklik_obj, 'kulaklik2':kulaklik2})

def other_view(request):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    return render(request, "sarj.html", {'apple2': apple2,'xiaomi2': xiaomi2,'oppo2': oppo2,'other2': other2,'huawei2': huawei2,'kulaklik2': kulaklik2,'macbook2': macbook2,'realme2': realme2,'samsung2': samsung2})

def other_detay(request, other_id):
    apple2 = apple.objects.all()
    xiaomi2 = xiaomi.objects.all()
    oppo2 = oppo.objects.all()
    other2 = other.objects.all()
    huawei2 = huawei.objects.all()
    kulaklik2 = kulaklik.objects.all()
    macbook2 = macbook.objects.all()
    realme2 = realme.objects.all()
    samsung2 = samsung.objects.all()
    media_url2 = os.path.join('/', 'media')
    other_obj = get_object_or_404(other, pk=other_id)
    return render(request, 'sarj_detay.html', {'other': other_obj, 'other2':other2})


def teslimat(request):

    return render(request, "teslimat.html")


def gizlilik(request):

    return render(request, "gizlilik.html")
    
def kullanım(request):

    return render(request, "kullanım.html")

def iade(request):

    return render(request, "iade.html")

def Iletisim(request):
    # İletişim sayfasının işlemleri buraya gelecek
    return render(request, 'iletisim.html')


