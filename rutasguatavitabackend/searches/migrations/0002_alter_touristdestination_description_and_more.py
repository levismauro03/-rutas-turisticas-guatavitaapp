# Generated by Django 4.1.1 on 2022-09-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristdestination',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='touristdestination',
            name='ubication',
            field=models.CharField(max_length=100),
        ),
    ]
