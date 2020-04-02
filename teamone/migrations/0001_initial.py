# Generated by Django 2.2.8 on 2020-04-02 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schronisko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('haslo', models.CharField(max_length=30)),
                ('telefon', models.CharField(max_length=15)),
                ('adres', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('haslo', models.CharField(max_length=30)),
                ('lajk', models.BooleanField()),
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
                ('uzytkownikID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamone.Uzytkownik')),
                ('zwierzeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamone.Zwierze')),
            ],
        ),
    ]
