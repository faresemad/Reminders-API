# Generated by Django 3.2 on 2023-04-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]