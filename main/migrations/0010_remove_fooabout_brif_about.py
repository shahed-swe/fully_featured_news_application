# Generated by Django 3.0.5 on 2020-05-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_fooabout_brif_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooabout',
            name='brif_about',
        ),
    ]