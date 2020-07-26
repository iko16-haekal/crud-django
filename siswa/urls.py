from django.contrib import admin
from django.urls import path
from dataSiswa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', siswa),
    path('siswa/', siswa),
    path('siswa/<int:id_siswa>', detailSiswa, name='detail_siswa'),
    path('siswa/tambah/', tambahSiswa, name='tambah_siswa'),
    path('siswa/ubah/<int:id_siswa>', ubahSiswa, name='ubah_siswa'),
    path('siswa/hapus/<int:id_siswa>', hapusSiswa, name='hapus_siswa')
]
