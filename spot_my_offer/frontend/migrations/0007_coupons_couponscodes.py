# Generated by Django 4.0.4 on 2022-06-02 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coupon_title', models.CharField(max_length=200, null=True)),
                ('coupon_status', models.CharField(choices=[('active', 'Active'), ('pending', 'Pending')], default='active', max_length=7)),
                ('discount_type', models.CharField(choices=[('percentage', 'Percentage')], default='percentage', max_length=17)),
                ('generated_items', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
        ),
        migrations.CreateModel(
            name='CouponsCodes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coupon_code', models.CharField(max_length=20)),
                ('coupon_used_status', models.CharField(choices=[('not_used', 'Not Used'), ('used', 'Used')], default='not_used', max_length=17)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.coupons')),
            ],
        ),
    ]
