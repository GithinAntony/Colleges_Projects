# Generated by Django 3.0.4 on 2020-03-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_gallery_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('streaming_file', models.TextField(null=True)),
                ('text', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]