# Generated by Django 3.0.3 on 2020-02-22 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='owner',
        ),
    ]