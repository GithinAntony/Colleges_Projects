# Generated by Django 3.0.2 on 2020-03-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20200308_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='type',
            field=models.CharField(choices=[('restaurant', 'Restaurant'), ('fashion', 'Fashion'), ('jewellery', 'Jewellery')], default='restaurant', max_length=15),
        ),
    ]
