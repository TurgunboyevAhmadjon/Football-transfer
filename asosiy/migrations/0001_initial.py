# Generated by Django 4.0.6 on 2022-08-29 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('president', models.CharField(max_length=50)),
                ('coach', models.CharField(max_length=100)),
                ('davlat', models.CharField(max_length=50)),
                ('yil', models.DateTimeField()),
                ('record_transfer', models.CharField(max_length=100)),
                ('record_arrival', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('yosh', models.IntegerField()),
                ('davlat', models.CharField(max_length=50)),
                ('pozitsiya', models.IntegerField()),
                ('narx', models.IntegerField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.clubs')),
            ],
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tah_narx', models.IntegerField()),
                ('narx', models.IntegerField()),
                ('mavsum', models.CharField(max_length=200)),
                ('all_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='al_from', to='asosiy.clubs')),
                ('all_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='al_to', to='asosiy.clubs')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.player')),
            ],
        ),
    ]
