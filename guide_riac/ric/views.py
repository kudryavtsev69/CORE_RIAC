from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Radar
from .forms import AddRadar


def index(request):
    return render(request, 'index.html', {})


def list_radar(request):
    all_radar = Radar.objects.all()
    return render(request, 'list_radar.html', {'all_radar': all_radar})


def radar_detail(request, radar):
    radar = get_object_or_404(Radar, slug=radar)
    return render(request, 'radar_detail.html', {'rls': radar})


def add_rls(request):
    if request.method == 'POST':
        add_form = AddRadar(request.POST, files=request.FILES)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, 'РЛС добавлена!')
        else:
            messages.error(request, 'РЛС не добавлена!')
            return HttpResponse(add_form.errors)
    else:
        add_form = AddRadar()
    return render(request, 'add_rls.html', {'add_form': add_form})

