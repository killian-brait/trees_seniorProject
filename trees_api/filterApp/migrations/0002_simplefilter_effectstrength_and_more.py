# Generated by Django 4.2.2 on 2023-06-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplefilter',
            name='effectStrength',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='simplefilter',
            name='effect',
            field=models.IntegerField(default=0),
        ),
    ]
