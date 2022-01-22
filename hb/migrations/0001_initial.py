# Generated by Django 3.0.2 on 2022-01-08 11:57

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
            name='Hydb',
            fields=[
                ('device_id', models.TextField(max_length=30, primary_key=True, serialize=False)),
                ('temp', models.FloatField(default=0.0)),
                ('temp_w', models.FloatField(default=0.0)),
                ('humid', models.IntegerField(default=0)),
                ('w_level', models.IntegerField(default=0)),
                ('pump', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hb.Hydb')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
