# Generated by Django 2.0.7 on 2019-01-30 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0004_auto_20190130_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured_jobs',
            name='jobs',
        ),
        migrations.AddField(
            model_name='featured_jobs',
            name='jobs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Jobs.Job'),
        ),
        migrations.RemoveField(
            model_name='hot_jobs',
            name='jobs',
        ),
        migrations.AddField(
            model_name='hot_jobs',
            name='jobs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Jobs.Job'),
        ),
    ]
