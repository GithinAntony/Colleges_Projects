from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class User(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    place = models.CharField(max_length=255, null=True)
    status_choices = [
        ('active', 'Active'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.name

class Shop(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    type_choices = [
        ('restaurant', 'Restaurant'),
        ('fashion', 'Fashion'),
        ('jewellery', 'Jewellery'),
    ]
    type = models.CharField(max_length=15, choices=type_choices, default="restaurant")
    about = models.TextField(null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    status_choices = [
        ('active', 'Active'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.name

class Admin(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class Offer(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    shopid = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    highlights = models.TextField(null=True)
    description = models.TextField(null=True)
    photo = models.TextField(null=True)
    actual_price = models.CharField(max_length=100, null=True)
    offer_price = models.CharField(max_length=100, null=True)
    termsandconditions = models.TextField(null=True)
    validity = models.CharField(max_length=100, null=True)
    couponcount = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    status_choices = [
        ('active', 'Active'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.title

class Orders(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    offerid = models.IntegerField(null=True)
    userid = models.IntegerField(null=True)
    shopid = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    address = models.TextField(null=True)
    couponcode = models.CharField(max_length=100, null=True)
    timestamp = models.CharField(max_length=100, null=True)
    active = models.IntegerField(null=True)
    redeem_time = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ordernumber

class Place(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    offerid = models.IntegerField(null=True)
    userid = models.IntegerField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.offerid

class Contact_message(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Coupons(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    coupon_title = models.CharField(max_length=200, null=True)
    status_choices = [
        ('active', 'Active'),
        ('pending', 'Pending'),
    ]
    coupon_status = models.CharField(max_length=7, choices=status_choices, default="active")
    status_choices = [
        ('percentage', 'Percentage'),
    ]
    discount_type = models.CharField(max_length=17, choices=status_choices, default="percentage")
    discount_percentage = models.IntegerField(null=False, default=0)
    append_text = models.CharField(max_length=10, null=True)
    generated_items = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return self.coupon_title

class CouponsCodes(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupons, on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=200, null=False)
    status_choices = [
        ('not_used', 'Not Used'),
        ('used', 'Used'),
    ]
    coupon_used_status = models.CharField(max_length=17, choices=status_choices, default="not_used")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return self.coupon_code
