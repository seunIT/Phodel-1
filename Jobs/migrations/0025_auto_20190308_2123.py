# Generated by Django 2.0.7 on 2019-03-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0024_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='job',
            field=models.PositiveIntegerField(default=0),
        ),
    ]