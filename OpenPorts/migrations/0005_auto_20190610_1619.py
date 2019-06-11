# Generated by Django 2.2.2 on 2019-06-10 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OpenPorts', '0004_auto_20190605_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuredPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secured_ports', models.CharField(max_length=260000)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnsecuredPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unsecured_ports', models.CharField(max_length=260000)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='unsecuredip',
            name='ip_addr',
        ),
        migrations.RemoveField(
            model_name='unsecuredip',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='host',
            old_name='user_id',
            new_name='added_by',
        ),
        migrations.RenameField(
            model_name='host',
            old_name='init_dt',
            new_name='added_on',
        ),
        migrations.RenameField(
            model_name='scan',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='host',
            name='id',
        ),
        migrations.RemoveField(
            model_name='host',
            name='ip_addr',
        ),
        migrations.AddField(
            model_name='host',
            name='host_id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='host_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='ip',
            field=models.GenericIPAddressField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='modified_on',
            field=models.DateField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='provider',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='secure_proxy_ip',
            field=models.GenericIPAddressField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='unsecure_proxy_ip',
            field=models.GenericIPAddressField(default=None),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SecuredIP',
        ),
        migrations.DeleteModel(
            name='UnsecuredIP',
        ),
        migrations.AddField(
            model_name='unsecuredport',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpenPorts.Host'),
        ),
        migrations.AddField(
            model_name='securedport',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OpenPorts.Host'),
        ),
    ]
