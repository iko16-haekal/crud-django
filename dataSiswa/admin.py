from django.contrib import admin
from dataSiswa.models import Jurusan, Siswa
# Register your models here.


class SiswaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'telepon', 'email', 'jurusan']
    search_fields = ['nama', 'telepon', 'email']
    list_per_page = 5
    list_filter = ['jurusan']


admin.site.register(Jurusan)
admin.site.register(Siswa, SiswaAdmin)
