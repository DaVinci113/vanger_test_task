from django.shortcuts import render

from .models import SliderImage


def index(request):
    images = SliderImage.objects.filter(is_active=True).order_by("order", "-created_at")
    return render(request, "slider/index.html", {"images": images})

