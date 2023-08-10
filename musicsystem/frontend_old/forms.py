from django.db import models
from django import forms
from .models import *
from django.core.validators import FileExtensionValidator


class LoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(email=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(username=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data


class AddNewPlaceForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Establishment Name'}))
    overview = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    type_choices = [
        ('Beach', 'Beach'),
        ('Hill Station', 'Hill Station'),
        ('Other', 'other'),
    ]
    type = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Establishment Type'}))
    main_photo = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    place = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Place', 'list': 'placeslist'}))
    amenities = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Amenities', 'list': 'amenitieslist'}))
    besttime = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Best time to visit'}))
    howtoreach = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'How to Reach'}))
    nativelanguage = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Native Language'}))
    latitude = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Latitude'}))
    longitude = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Longitude'}))
    description = overview = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Description', 'rows': '3'}))


class MyProfileForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))


class EventForm(forms.Form):
    event = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Event name'}))
    date = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Date'}))
    time = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Time'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Location'}))
    contact = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    amount = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Amount'}))
    seat = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Avaliable Seats'}))
    more = forms.CharField(max_length=100, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Details'}))
    main_photo = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])


class InstrumentsForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Instrument name'}))
    amount = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                              error_messages={'invalid': ("This value may contain only numbers.")},
                              widget=forms.TextInput(
                                  attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Amount'}))
    avaliable = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Avaliable No'}))
    main_photo = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])


class OrderForm(forms.Form):
    quantity_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '9'),
        ('10', '10'),
    ]
    quantity = forms.CharField(max_length=20, widget=forms.Select(choices=quantity_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Establishment Type', 'onchange': 'calculate_total(this.value)' }))
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full name'}))
    address = forms.CharField(max_length=100, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'address'}))
    payment_choices = [
        ('credit_card', 'Credit card'),
        ('debit_card', 'Debit card')
    ]
    payment_type = forms.CharField(max_length=20, widget=forms.Select(choices=payment_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Payment Type' }))
    name_on_card = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Name on Card'}))
    credit_card_number = forms.RegexField(regex=r'^[0-9]+$', max_length=20,
                                 error_messages={'invalid': ("This value may contain only numbers.")},
                                 widget=forms.TextInput(
                                     attrs={'autocomplete': 'off', 'class': 'form-control',
                                            'placeholder': 'Credit Card Number'}))
    expiration = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Expiration'}))
    cvv = forms.RegexField(regex=r'^[0-9]+$', max_length=20,
                                 error_messages={'invalid': ("This value may contain only numbers.")},
                                 widget=forms.TextInput(
                                     attrs={'autocomplete': 'off', 'class': 'form-control',
                                            'placeholder': 'CVV'}))

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Message'}))

class GalleryForm(forms.Form):
    photos = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    text = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Text'}))