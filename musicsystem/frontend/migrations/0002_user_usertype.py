# Generated by Django 3.0.2 on 2020-02-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
