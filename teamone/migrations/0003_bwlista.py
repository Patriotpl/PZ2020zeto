# Generated by Django 2.2.7 on 2020-05-05 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamone', '0002_auto_20200504_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='BWLista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_user', models.CharField(max_length=100)),
                ('czyLike', models.BooleanField()),
                ('zwierzeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamone.Zwierze')),
            ],
        ),
    ]