# Generated by Django 5.1.5 on 2025-02-06 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfect_Nannies_App', '0003_remove_nanny_charge_alter_guardian_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nanny',
            name='guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Perfect_Nannies_App.guardian'),
        ),
    ]
