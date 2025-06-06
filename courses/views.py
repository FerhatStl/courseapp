from django.http import HttpResponse
from django.shortcuts import render

def kurslar(request):
    return HttpResponse("kurs listesi")

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(request, category_name):
    text = ""

    if(category_name == "programlama"):
        text = "programlama kategorisine ait kurslar"
    elif (category_name == "web-gelistirme"):
        text = "web-gelistirme kategorisine ait kurslar"
    else:
        text = "yanlış kategori seçimi"
    return HttpResponse(text)

def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)