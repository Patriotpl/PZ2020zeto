from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class Schronisko(models.Model):
    login = models.CharField(max_length=30, null=False)
    telefon = models.CharField(max_length=15)
    adres = models.CharField(max_length=30)

class Zwierze(models.Model):
    schroniskoID = models.ForeignKey(Schronisko, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=30)
    gatunek = models.CharField(max_length=30)
    zdjecie = models.CharField(max_length=50)
    opis = models.CharField(max_length=200)
    czyDuzeMieszkanie = models.BooleanField()
    czyDuzoCzasu = models.BooleanField()
    czyDzieci = models.BooleanField()

class Lista(models.Model):
    uzytkownikID = models.ForeignKey(User, on_delete=models.CASCADE)
    zwierzeID = models.ForeignKey(Zwierze, on_delete=models.CASCADE)

class Preferencje(models.Model):
    token_user = models.CharField(max_length=100, primary_key=True)
    czyDuzeMieszkanie = models.BooleanField()
    czyDuzoCzasu = models.BooleanField()
    czyDzieci = models.BooleanField()

