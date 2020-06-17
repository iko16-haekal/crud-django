from django.forms import ModelForm
from django import forms
from dataSiswa.models import Siswa


class FormSiswa(ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control'}),
            'email': forms.EmailInput({'class': 'form-control'}),
            'telepon': forms.NumberInput({'class': 'form-control'}),
            'jurusan': forms.Select({'class': 'form-control'}),
        }
