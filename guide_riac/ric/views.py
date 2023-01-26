from django.shortcuts import render, get_object_or_404
from .models import Radar


def index(request):
    return render(request, 'index.html', {})


def list_radar(request):
    all_radar = Radar.objects.all()
    return render(request, 'list_radar.html', {'all_radar': all_radar})


def radar_detail(request, radar):
    radar = get_object_or_404(Radar, slug=radar)
    return render(request, 'radar_detail.html', {'rls': radar})
