# Generated by Django 3.1.2 on 2020-10-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='line',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
