# Generated by Django 3.0.5 on 2020-05-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200501_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='ln',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.CharField(max_length=100, null=True),
        ),
    ]