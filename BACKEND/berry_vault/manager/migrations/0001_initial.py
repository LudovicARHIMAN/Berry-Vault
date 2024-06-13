# Generated by Django 5.0.4 on 2024-06-13 19:31

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vault',
            fields=[
                ('vault_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vault_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vault', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('pass_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('favorite', models.BooleanField(default=False)),
                ('vault', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.vault')),
            ],
        ),
    ]