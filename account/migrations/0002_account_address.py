# Generated by Django 4.1.4 on 2023-03-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
