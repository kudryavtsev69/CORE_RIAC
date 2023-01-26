from django.contrib import admin
from .models import Radar


# Register your models here.
@admin.register(Radar)
class RadarAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'data', 'image',)
    prepopulated_fields = {'slug': ('title',)}
