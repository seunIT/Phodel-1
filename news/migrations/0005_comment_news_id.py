# Generated by Django 2.1.5 on 2019-02-17 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='News_Id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]