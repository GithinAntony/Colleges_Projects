# Generated by Django 2.2.13 on 2020-07-13 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Offer',
            new_name='offer',
        ),
    ]