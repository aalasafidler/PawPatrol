# Generated by Django 2.1.3 on 2018-11-21 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20181108_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
