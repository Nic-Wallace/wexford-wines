# Generated by Django 3.2.25 on 2025-03-10 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='colour',
            new_name='wine_colour',
        ),
    ]
