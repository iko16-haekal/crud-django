from django.db import models

# Create your models here.


class Jurusan(models.Model):
    jurusan = models.CharField(max_length=30)

    def __str__(self):
        return self.jurusan


class Siswa(models.Model):
    nama = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    telepon = models.BigIntegerField()
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
