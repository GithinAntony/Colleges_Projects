# Generated by Django 4.0.4 on 2022-06-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20200309_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
