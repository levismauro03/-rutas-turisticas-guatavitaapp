# Generated by Django 4.1.1 on 2022-09-07 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('ubication', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
