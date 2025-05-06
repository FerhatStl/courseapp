from django.http import HttpResponse
from django.urls import path
from .views import home, kurslar
    # http://127.0.0.1:8000/        => anasayfa
    # http://127.0.0.1:8000/home    => anasayfa
    # http://127.0.0.1:8000/kurslar => kurs listesi



urlpatterns = [
    path("", home),
    path("anasayfa", home),
    path("kurslar", kurslar)
]
