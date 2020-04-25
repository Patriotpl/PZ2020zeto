# Generated by Django 2.2.8 on 2020-04-18 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferencje',
            fields=[
                ('token_user', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('czyDuzeMieszkanie', models.BooleanField()),
                ('czyDuzoCzasu', models.BooleanField()),
                ('czyDzieci', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Schronisko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('telefon', models.CharField(max_length=15)),
                ('adres', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Zwierze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('gatunek', models.CharField(max_length=30)),
                ('zdjecie', models.CharField(max_length=50)),
                ('opis', models.CharField(max_length=200)),
                ('czyDuzeMieszkanie', models.BooleanField()),
                ('czyDuzoCzasu', models.BooleanField()),
                ('czyDzieci', models.BooleanField()),
                ('schroniskoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamone.Schronisko')),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzytkownikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zwierzeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamone.Zwierze')),
            ],
        ),
    ]
