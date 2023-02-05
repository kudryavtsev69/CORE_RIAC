from django import forms
from .models import Radar


class AddRadar(forms.ModelForm):
    class Meta:
        model = Radar
        fields = ('title', 'body', 'image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название РЛС'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание РЛС'}),
        }
