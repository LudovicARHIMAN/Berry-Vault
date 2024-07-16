# Generated by Django 5.0.7 on 2024-07-15 18:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_remove_vault_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vault',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vault', to=settings.AUTH_USER_MODEL),
        ),
    ]