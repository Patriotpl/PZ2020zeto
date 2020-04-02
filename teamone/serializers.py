from rest_framework import serializers
from .models import Schronisko, Zwierze, Uzytkownik, Lista
from django.contrib.auth.models import User


class SchroniskoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Schronisko
        fields = '__all__'

class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = '__all__'

class ZwierzeSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Zwierze
        fields = '__all__'

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'