# Generated by Django 5.2.1 on 2025-05-11 14:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_gasto_created_at_gasto_grupo_gasto_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
