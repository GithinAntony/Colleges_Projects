# Generated by Django 2.2.13 on 2020-07-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20200703_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]