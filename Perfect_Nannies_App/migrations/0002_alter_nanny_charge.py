# Generated by Django 5.1.5 on 2025-02-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfect_Nannies_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nanny',
            name='charge',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
