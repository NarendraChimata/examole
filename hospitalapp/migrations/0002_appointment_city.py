# Generated by Django 3.2.18 on 2023-05-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
