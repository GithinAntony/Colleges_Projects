from django.db import models
from django import forms
from .models import *
from django.core.validators import FileExtensionValidator

class LoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Password'}))


class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Address', 'rows': '3'}))

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


class ShopRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Shop Name'}))
    type_choices = [
        ('restaurant', 'Restaurant'),
        ('fashion', 'Fashion'),
        ('jewellery', 'Jewellery'),
    ]
    type = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control input-lg',
                                                                     'placeholder': 'Establishment type'}))
    about = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'About', 'rows': '3'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Email'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Phone number'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Address', 'rows': '3'}))
    latitude = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Latitude'}))
    longitude = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Longitude'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Shop.objects.filter(email=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Shop.objects.filter(username=self.cleaned_data['username'])
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

class PlaceForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Add new places'}))

    def clean_name(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Place.objects.filter(name=self.cleaned_data['name'])
        if existing.exists():
            raise forms.ValidationError(("A name with that places already exists."))
        else:
            return self.cleaned_data['name']

class AddNewOfferForm(forms.Form):
    offer_photo = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'title'}))
    highlights = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Highlights', 'rows': '3'}))
    description = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Description', 'rows': '3'}))
    actual_price = forms.RegexField(regex=r'^[0-9]+$', max_length=8,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Actual Price'}))
    offer_price = forms.RegexField(regex=r'^[0-9]+$', max_length=8,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Offer Price'}))
    validity = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Validity', 'id' : 'validity'}))
    termsandconditions = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'terms and conditions', 'rows': '3'}))
    place = forms.ModelChoiceField(queryset=Place.objects.all(), initial=0, widget=forms.Select(attrs={'autocomplete': 'off', 'class': 'form-control input-lg',
                                                                     'placeholder': 'Place'}) )

class UserOfferPayment(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Card Name'}))
    card = forms.RegexField(regex=r'^[0-9]+$', max_length=15,
                             error_messages={'invalid': ("This value may contain only numbers.")},widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Card Number'}))
    expdate = forms.RegexField(regex=r'^[0-9]+$', max_length=2,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Expiry Month'}))
    expyear = forms.RegexField(regex=r'^[0-9]+$', max_length=4,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Expiry Year'}))
    cvv = forms.RegexField(regex=r'^[0-9]+$', max_length=3,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'CVV'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Address'}))

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Message'}))