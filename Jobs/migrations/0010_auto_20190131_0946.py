# Generated by Django 2.0.7 on 2019-01-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0009_auto_20190130_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Job_Description',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='town',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='personal_note',
            field=models.CharField(max_length=500),
        ),
    ]
