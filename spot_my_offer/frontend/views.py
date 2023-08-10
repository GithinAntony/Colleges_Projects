from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import uuid
import random as r


# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if Admin.objects.filter(username=data_record['username']) and Admin.objects.filter(
                    password=data_record['password']):
                user_details = Admin.objects.get(username=data_record['username'], password=data_record['password'])
                request.session['is_logged_in'] = True
                request.session['email'] = ''
                request.session['full_name'] = ''
                request.session['user_id'] = user_details.id
                request.session['username'] = user_details.username
                request.session['usertype'] = 'admin'
                return redirect('/admin-dashboard')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/admin')
    context = {'form': form}
    return render(request, 'admin-login.html',context)

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_shop(request):
    record_details = Shop.objects.all()
    context = {'record_details': record_details}
    return render(request, 'admin-shop.html', context)

def admin_users(request):
    record_details = User.objects.all()
    context = {'record_details': record_details}
    return render(request, 'admin-users.html', context)

def admin_offers(request):
    record_details = Offer.objects.all()
    context = {'record_details': record_details}
    return render(request, 'admin-offers.html', context)

def admin_places(request):
    form = PlaceForm()
    places = Place.objects.all()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            place = Place(
            name=data_record['name']
            )
            place.save()
            messages.success(request, 'Places added successfully!')
            return redirect('/admin-places')
    context = {'places': places, 'form':form  }
    print(form)
    return render(request, 'admin-places.html', context)

def admin_record_status(request, id, slug1, slug2):
    if slug1 == 'users':
      record = User.objects.get(id=id)
      record.status = slug2
      record.save()
      messages.error(request, 'User status updated!')
      return redirect('/admin-users')
    elif slug1 == 'shop':
        record = Shop.objects.get(id=id)
        record.status = slug2
        record.save()
        messages.error(request, 'Shop status updated!')
        return redirect('/admin-shops')
    elif slug1 == 'place':
        record = Place.objects.get(id=id)
        record.status = slug2
        record.save()
        messages.error(request, 'Offers status updated!')
        return redirect('/offers-places')

def admin_record_delete(request, id, slug1):
    if slug1 == 'users':
       User.objects.filter(id=id).delete()
       messages.error(request, 'User deleted!')
       return redirect('/admin-users')
    elif slug1 == 'shop':
      Shop.objects.filter(id=id).delete()
      messages.error(request, 'User deleted!')
      return redirect('/admin-shops')
    elif slug1 == 'place':
        Place.objects.filter(id=id).delete()
        messages.error(request, 'Place deleted!')
        return redirect('/admin-places')

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username']) and User.objects.filter(
                    password=data_record['password']):
                user_details = User.objects.get(username=data_record['username'], password=data_record['password'])
                if user_details.status == 'active':
                    request.session['is_logged_in'] = True
                    request.session['email'] = user_details.email
                    request.session['full_name'] = user_details.name
                    request.session['user_id'] = user_details.id
                    request.session['username'] = user_details.username
                    request.session['usertype'] = 'user'
                    return redirect('/user-dashboard')
                else:
                   messages.error(request, 'User is suspended. Contact the admin!')
                   return redirect('/user-login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/user-login')
    context = {'form': form}
    return render(request, 'user-login.html', context)

def user_register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            user = User(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            status='pending',
            )
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/user-login')
    context = {'form': form}
    return render(request, 'user-register.html', context)

def shop_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if Shop.objects.filter(username=data_record['username']) and Shop.objects.filter(
                    password=data_record['password']):
                user_details = Shop.objects.get(username=data_record['username'], password=data_record['password'])
                if user_details.status == 'active':
                        request.session['is_logged_in'] = True
                        request.session['email'] = user_details.email
                        request.session['full_name'] = user_details.name
                        request.session['user_id'] = user_details.id
                        request.session['username'] = user_details.username
                        request.session['usertype'] = 'shop'
                        return redirect('/shop-dashboard')
                else:
                        messages.error(request, 'User is suspended. Contact the admin!')
                        return redirect('/shop-login')
            else:
                messages.error(request, 'Invalid Credentials!')
                return redirect('/shop-login')
    context = {'form': form}
    return render(request, 'shop-login.html', context)

def shop_register(request):
    form = ShopRegisterForm()
    if request.method == 'POST':
        form = ShopRegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            shop = Shop(
            name=data_record['name'],
            type=data_record['type'],
            about=data_record['about'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            latitude=data_record['latitude'],
            longitude=data_record['longitude'],
            status='pending',
            )
            shop.save()
            messages.success(request, 'shop registered successfully!')
            return redirect('/shop-login')
    context = {'form': form}
    return render(request, 'shop-register.html', context)


def shop_dashboard(request):
    offer_details = Offer.objects.filter(shopid=request.session['user_id']).count()
    order_details = Orders.objects.filter(shopid=request.session['user_id']).count()
    context = {'offer_details': offer_details, 'order_details': order_details}
    return render(request, 'shop-dashboard.html',context )

def shop_profile(request):
    return render(request, 'shop-profile.html' )

def shop_my_offers(request):
    offer = Offer.objects.filter(shopid=request.session['user_id'])
    context = {'offer': offer}
    return render(request, 'shop-my-offers.html', context )

def shop_offer_delete(request, id):
    Offer.objects.filter(id=id).delete()
    messages.error(request, 'Offer deleted!')
    return redirect('/shop-my-offers')

def shop_add_offers(request):
    form = AddNewOfferForm()
    if request.method == 'POST':
        form = AddNewOfferForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['offer_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            offer = Offer(
            shopid=request.session['user_id'],
            title=data_record['title'],
            highlights=data_record['highlights'],
            description=data_record['description'],
            photo=fs.url(file_name),
            actual_price=data_record['actual_price'],
            offer_price=data_record['offer_price'],
            termsandconditions=data_record['termsandconditions'],
            validity=data_record['validity'],
            place=data_record['place'],
            status='active',
            )
            offer.save()
            messages.success(request, 'Offer added successfully!')
            return redirect('/shop-my-offers')
    context = {'form': form}
    return render(request, 'shop-add-offers.html', context )

def user_dashboard(request):
    return render(request, 'dashboard.html' )

def user_offer(request):
    if request.method == 'POST':
       request.session['location'] = request.POST['location']
       return redirect('/users-offer-cart')
    place = Place.objects.all()
    context = {'place': place}
    return render(request, 'select_location.html',context)

def user_offer_cart(request):
    offer = Offer.objects.filter(place=request.session['location'])
    context = {'offer': offer}
    return render(request, 'user-offer-cart.html', context)

def user_offer_details(request, id):
    offer = Offer.objects.get(id=id)
    if request.method == 'POST':
        data_record = request.POST
        coupon_code = data_record['coupon_code']
        # Check coupon code is valid
        coupon_id = 0
        if coupon_code != '':
            check_coupon=CouponsCodes.objects.filter(coupon_code=coupon_code,coupon_used_status='not_used',shop_id=offer.shopid).all()
            if check_coupon.count() > 0:
                for i in check_coupon:
                    coupon_id = i.id
                return redirect('/user-offer-cart-payment/'+str(id)+'/'+str(coupon_id))
            else:
                messages.error(request, 'Your coupon code is Invalid! Try a new one or leave the coupon box blank to continue without applying coupon.. ')
                return redirect('/user-offer-details/'+str(id))
        else:
            return redirect('/user-offer-cart-payment/'+str(id)+'/'+str(coupon_id))
    context = {'i': offer}
    return render(request, 'user-offer-details.html', context)

def user_offer_payment(request, id, discount_id):
    offer = Offer.objects.get(id=id)
    form = UserOfferPayment()
    discount_details = ''
    discounted_amount  = offer.offer_price
    if discount_id > 0:
        discount_details = CouponsCodes.objects.get(id=discount_id)
        discounted_amount = int(offer.offer_price) - ( int(offer.offer_price) * (discount_details.coupon.discount_percentage/100))
    if request.method == 'POST':
        form = UserOfferPayment(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            order = Orders(
            offerid=id,
            userid=request.session['user_id'],
            shopid=offer.shopid,
            price=discounted_amount,
            address=data_record['address'],
            )
            order.save()
            if discount_id > 0:
                 discount_details.coupon_used_status = 'used'
                 discount_details.save()
            messages.success(request, 'Payment was successful!')
            return redirect('/users-offer-cart')
    context = {'offer': offer, 'discount_details':discount_details, 'discounted_amount':discounted_amount, 'form': form}
    return render(request, 'user-offer-payment.html', context)

def user_my_orders(request):
    orders = Orders.objects.filter(userid=request.session['user_id'])
    """"
    shop_details = Shop.objects.get(id=orders.shopid)
    offer_details = Offer.objects.get(id=orders.offerid)
    """
    context = {'orders':orders }
    return render(request, 'my-orders.html', context )

def logout(request):
    del request.session['is_logged_in']
    del request.session['username']
    del request.session['usertype']
    return redirect('/home')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            contact = Contact_message(
            name=data_record['name'],
            email=data_record['email'],
            message=data_record['message'],
            )
            contact.save()
            messages.success(request, 'Message registered successfully!')
            return redirect('/contact')
    context = {'form': form}
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')

def admin_contact_us(request):
    context = { 'contactus' : Contact_message.objects.filter() }
    return render(request, 'admin-contact.html',context)

def shop_my_coupons(request):
    coupons_main=Coupons.objects.filter(shop_id=request.session['user_id']).all()
    context = { 'coupons':coupons_main }
    return render(request, 'shop-my-coupons.html',context)

def shop_add_coupons(request):
    if request.method == 'POST':
        data_record = request.POST
        append_text = data_record['append_text'].upper().replace(' ', '')
        add_coupon= Coupons(
        shop=Shop.objects.get(id=request.session['user_id']),
        coupon_title=data_record['coupon_title'],
        coupon_status=data_record['coupon_status'],
        discount_type='percentage',
        discount_percentage=data_record['discount_percentage'],
        append_text=append_text,
        generated_items=data_record['no_of_coupon_code'],
        )
        add_coupon.save()
        no_of_coupon_code = int(data_record['no_of_coupon_code'])
        LastInsertId=Coupons.objects.latest('id')
        for i in range(no_of_coupon_code):
            val=generate_uuid()
            _coupon_code=CouponsCodes(
            shop=Shop.objects.get(id=request.session['user_id']),
            coupon = LastInsertId,
            coupon_code = str(append_text)+str(val),
            )
            _coupon_code.save()
        messages.success(request, 'Coupon Generated')
        return redirect('/shop-view-coupons/'+str(LastInsertId.id))
    return render(request, 'shop-add-coupons.html')

def generate_uuid():
        random_string = ''
        random_str_seq = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"
        uuid_format = [8]
        for n in uuid_format:
            for i in range(0,n):
                random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
            if n != 12:
                random_string += ''
        return random_string.upper()

def shop_view_coupons(request, id):
    coupons_main=Coupons.objects.get(id=id)
    coupon_codes=CouponsCodes.objects.filter(coupon_id=id,shop_id=request.session['user_id']).all()
    if request.method == 'POST':
        data_record = request.POST
        coupons_main.coupon_title = data_record['coupon_title']
        coupons_main.coupon_status = data_record['coupon_status']
        coupons_main.discount_percentage = data_record['discount_percentage']
        coupons_main.save()
        messages.success(request, 'Coupons updated successfully!')
        return redirect('/shop-view-coupons/'+str(id))
    context = { 'coupons':coupons_main, 'coupon_codes':coupon_codes }
    return render(request, 'shop-view-coupons.html', context)

def shop_delete_coupons(request, id):
    Coupons.objects.get(id=id).delete()
    CouponsCodes.objects.filter(coupon_id=id).delete()
    messages.error(request, 'Coupon deleteed successfully!')
    return redirect('/shop-my-coupons')
