# Generated by Django 2.2.13 on 2020-07-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20200702_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='timestamp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]