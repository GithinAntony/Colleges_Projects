# Generated by Django 3.0.2 on 2020-03-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20200308_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('suspend', 'Suspend')], default='active', max_length=7),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]