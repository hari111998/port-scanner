# Generated by Django 2.2.2 on 2019-06-11 06:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OpenPorts', '0005_auto_20190610_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenPortResult',
            fields=[
                ('res_id', models.IntegerField(primary_key=True, serialize=False)),
                ('open_ports', models.CharField(max_length=330000)),
                ('closed_ports', models.CharField(max_length=330000)),
                ('started_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('runtime', models.CharField(max_length=255)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpenPorts.Host')),
            ],
        ),
        migrations.CreateModel(
            name='SecurePortResult',
            fields=[
                ('res_id', models.IntegerField(primary_key=True, serialize=False)),
                ('open_ports', models.CharField(max_length=330000)),
                ('closed_ports', models.CharField(max_length=330000)),
                ('started_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('runtime', models.CharField(max_length=255)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpenPorts.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('setting_id', models.IntegerField(primary_key=True, serialize=False)),
                ('threads', models.IntegerField(blank=True, default=100)),
                ('timeout', models.IntegerField(blank=True, default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='UnsecuredPort',
            new_name='OpenPort',
        ),
        migrations.DeleteModel(
            name='Scan',
        ),
    ]
