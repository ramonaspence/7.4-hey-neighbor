# Generated by Django 3.0.3 on 2020-02-27 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools', '0005_auto_20200223_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='borrowing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp', to=settings.AUTH_USER_MODEL),
        ),
    ]
