# Generated by Django 3.0.5 on 2020-05-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_fooabout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fooAbout',
        ),
        migrations.AddField(
            model_name='main',
            name='about',
            field=models.TextField(null=True),
        ),
    ]