# Generated by Django 5.0.7 on 2024-07-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_rename_id_appuser_user_id_appuser_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
