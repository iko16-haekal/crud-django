from django.shortcuts import render, redirect
from django.contrib import messages
from dataSiswa.models import Siswa
from dataSiswa.forms import FormSiswa
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def siswa(request):
    konteks = {
        'siswa': Siswa.objects.all()
    }
    return render(request, 'siswa.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def detailSiswa(request, id_siswa):
    konteks = {'siswa': Siswa.objects.get(id=id_siswa)}
    return render(request, 'detail.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambahSiswa(request):
    if request.POST:
        form = FormSiswa(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "data berhasil ditambahkan")
            return redirect('/siswa/')
    konteks = {'form': FormSiswa()}
    return render(request, 'tambah.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def ubahSiswa(request, id_siswa):
    siswa = Siswa.objects.get(id=id_siswa)
    if request.POST:
        form = FormSiswa(request.POST, instance=siswa)
        if form.is_valid:
            form.save()
            messages.success(request, "data berhasil diubah")
            return redirect('/siswa/')

    konteks = {'form': FormSiswa(instance=siswa), 'siswa': siswa}
    return render(request, 'ubah.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapusSiswa(request, id_siswa):
    siswa = Siswa.objects.get(id=id_siswa)
    siswa.delete()
    messages.success(request, "data berhasil dihapus")
    return redirect('/siswa/')
