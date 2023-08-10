from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100,default='', null=False)
    email = models.CharField(max_length=255,default='', null=False)
    username = models.CharField(max_length=100,default='', null=False)
    password = models.CharField(max_length=500,default='', null=False)
    phone = models.CharField(max_length=15,default='', null=False)
    address = models.TextField(default='',null=False)
    usertype_choices = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    usertype = models.CharField(max_length=7, choices=usertype_choices, default="user")
    status_choices = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
    ]
    status = models.CharField(max_length=7, choices=status_choices, default="active")

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    location = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255, null=True)
    time = models.CharField(max_length=25, null=True)
    contact = models.CharField(max_length=255, null=True)
    amount = models.CharField(max_length=15, null=True)
    image = models.TextField(null=True)
    seat = models.CharField(max_length=255, null=True)
    event = models.CharField(max_length=255, null=True)
    more = models.TextField(null=True)

    def __str__(self):
        return self.location

class Itemadd(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=True)
    available = models.CharField(max_length=255, null=True)
    amount = models.CharField(max_length=25, null=True)
    image = models.TextField(null=True)

    def __str__(self):
        return self.name

class Music(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    lang = models.CharField(max_length=255, null=True)
    image = models.TextField(null=True)
    audio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.lang

class Mysq(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    image = models.TextField(null=True)
    username = models.CharField(max_length=255, null=True)
    dob = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    nationality = models.CharField(max_length=255, null=True)
    mobno = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.lang


class Order_1(models.Model):
    order_id = models.AutoField(primary_key=True, null=False)
    fullname = models.CharField(max_length=255, null=True)
    userid = models.IntegerField(null=True)
    quantity = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
    item_image = models.TextField(null=True)
    item_name = models.CharField(max_length=255, null=True)
    item_price = models.CharField(max_length=255, null=True)
    item_type = models.CharField(max_length=255, null=True)
    paid_by = models.CharField(max_length=255, null=True)
    card_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.fullname


class Payment(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    quantity = models.CharField(max_length=255, null=True)
    amount = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=255, null=True)
    total = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.lang

class Photos(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    photos = models.CharField(max_length=255, null=True)
    user_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.lang

class User_history(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    login_id = models.IntegerField(null=True)
    usage_track = models.TextField(null=True)
    usage_status = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.lang

class Contact_message(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    photos = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.photos

class Podcast(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    streaming_file = models.TextField(null=True)
    text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.streaming_file

