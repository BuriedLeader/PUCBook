# Generated by Django 4.0.5 on 2022-11-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PUCBook_Site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='bio',
            field=models.CharField(default='', max_length=200, verbose_name='bio'),
        ),
    ]