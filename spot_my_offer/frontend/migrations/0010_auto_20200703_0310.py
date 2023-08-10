# Generated by Django 2.2.13 on 2020-07-02 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20200703_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='shopid',
        ),
        migrations.AddField(
            model_name='offer',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Shop'),
        ),
    ]
