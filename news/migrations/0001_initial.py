# Generated by Django 3.0.5 on 2020-05-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_txt', models.TextField()),
                ('body_txt', models.TextField()),
                ('date', models.DateField()),
                ('image', models.TextField()),
                ('writter', models.CharField(max_length=50)),
            ],
        ),
    ]