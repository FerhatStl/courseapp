from django.http import HttpResponse
from django.shortcuts import render

def kurslar(request):
    return HttpResponse("kurs listesi")

def details(request):
    return HttpResponse("kurs detay sayfası")

def getCoursesByCategory(request, category):
    text = ""

    if(category == "programlama"):
        text = "programlama kategorisine ait kurslar"
    elif (category == "web-gelistirme"):
        text = "web-gelistirme kategorisine ait kurslar"
    else:
        text = "yanlış kategori seçimi"
    return HttpResponse(text)