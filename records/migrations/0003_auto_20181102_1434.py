# Generated by Django 2.0.6 on 2018-11-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_record_feedid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='amountDispensed',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='record',
            name='amountLeftOver',
            field=models.IntegerField(default='0'),
        ),
    ]
