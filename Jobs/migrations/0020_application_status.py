# Generated by Django 2.0.7 on 2019-02-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0019_auto_20190218_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
