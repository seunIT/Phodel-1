# Generated by Django 2.0.7 on 2019-02-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190204_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmodel',
            name='first_name',
            field=models.CharField(default='Name', max_length=20),
        ),
        migrations.AddField(
            model_name='pmodel',
            name='last_name',
            field=models.CharField(default='Name', max_length=20),
        ),
    ]
