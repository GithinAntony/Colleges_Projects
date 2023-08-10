from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about-us.html')

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            if User.objects.filter(username=data_record['username']) and User.objects.filter(
               password=data_record['password']):
               user_details = User.objects.get(username=data_record['username'],password=data_record['password'])
               if user_details.usertype == 'admin':
                   request.session['is_logged_in'] = True
                   request.session['email'] = user_details.email
                   request.session['full_name'] = user_details.name
                   request.session['user_id'] = user_details.id
                   request.session['username'] = user_details.username
                   request.session['usertype'] = user_details.usertype
                   return redirect('/admin-dashboard')
               else:
                 if user_details.status == 'active':
                     request.session['is_logged_in'] = True
                     request.session['email'] = user_details.email
                     request.session['full_name'] = user_details.name
                     request.session['user_id'] = user_details.id
                     request.session['username'] = user_details.username
                     request.session['usertype'] = user_details.usertype
                     return redirect('/user-dashboard')
                 else:
                   messages.error(request, 'User is suspended. Contact the admin!')
                   return redirect('/login')
            else:
               messages.error(request, 'Invalid Credentials!')
               return redirect('/login')
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data_record = form.cleaned_data
            user = User(
            name=data_record['name'],
            email=data_record['email'],
            username=data_record['username'],
            password=data_record['password'],
            phone=data_record['phone'],
            address=data_record['address'],
            status='active',
            usertype='user',
            )
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('/login')
    context = {'form': form}
    return render(request, 'register.html', context)
# User Processing

def user_dashboard(request):
    total_orders = Order_1.objects.filter(userid=request.session['user_id'])
    events = Order_1.objects.filter(item_type='event',userid=request.session['user_id'])
    instruments = Order_1.objects.filter(item_type='instrument',userid=request.session['user_id'])
    total_users = User.objects.filter()
    context = { 'total_orders':total_orders, 'events':events, 'instruments':instruments, 'total_users':total_users }
    return render(request, 'user-dashboard.html', context )

def user_past_orders(request):
    orders = Order_1.objects.filter(userid=request.session['user_id']).all()
    context = { 'orders':orders }
    return render(request, 'user-past-orders.html', context )

def user_book_events(request):
    event = Event.objects.all()
    context = {'event': event }
    return render(request, 'user-book-events.html', context )

def user_book_instruments(request):
    itemadd = Itemadd.objects.all()
    used_items =  Order_1.objects.filter(item_type='instrument').aggregate(Sum('quantity'))
    context = {'instruments': itemadd, 'used_items':used_items }
    return render(request, 'user-book-instruments.html', context )

def user_book_order_1(request,item_id, slug):
    if slug=="event":
     item =  Event.objects.filter(id=item_id)
     item_type = slug
    if slug == "instrument":
     item = Itemadd.objects.filter(id=item_id)
     item_type = slug
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            if slug == "event":
              date_record_2 = Event.objects.get(id=item_id)
              date_record_2_item_name = date_record_2.event
              date_record_2_item_image = date_record_2.image
              date_record_2_item_price = date_record_2.amount
            if slug == "instrument":
              date_record_2 = Itemadd.objects.get(id=item_id)
              date_record_2_item_name = date_record_2.name
              date_record_2_item_image = date_record_2.image
              date_record_2_item_price = date_record_2.amount
            data_record = form.cleaned_data
            order = Order_1(
            fullname=data_record['name'],
            userid=request.session['user_id'],
            quantity=data_record['quantity'],
            address=data_record['address'],
            item_image=date_record_2_item_image,
            item_name=date_record_2_item_name,
            item_price=date_record_2_item_price ,
            item_type=slug,
            paid_by=data_record['payment_type'],
            card_number=data_record['credit_card_number'],
            )
            order.save()
            request.session['item_id'] = order.pk
            messages.success(request, 'Payment processed successfully!')
            return redirect('/user-book-order-2')
    context = {'item': item, "item_type": item_type, "form": form }
    return render(request, 'user-book-order-1.html', context )

def user_book_order_2(request):
    order_1 = Order_1.objects.filter(order_id=request.session['item_id']).all()
    context = {'order': order_1 }
    return render(request, 'user-book-order-2.html', context )

def free_streaming(request):
    return render(request, 'podcast.html')

#admin processing

def admin_dashboard(request):
    total_orders = Order_1.objects.filter()
    events = Order_1.objects.filter(item_type='event')
    instruments = Order_1.objects.filter(item_type='instrument')
    total_users = User.objects.filter()
    context = { 'total_orders':total_orders, 'events':events, 'instruments':instruments, 'total_users':total_users }
    return render(request, 'admin-dashboard.html', context )

def admin_registered_users(request):
    user_details = User.objects.filter(usertype='user').all()
    context = {'user_details': user_details }
    return render(request, 'admin-registered-users.html', context )

def admin_registered_users_delete(request, user_id):
    User.objects.filter(id=user_id).delete()
    messages.error(request, 'User deleted!')
    return redirect('/admin-registered-users')

def admin_registered_users_status(request, user_id, slug):
    user = User.objects.get(id=user_id)
    user.status = slug
    user.save()
    messages.error(request, 'User status updated!')
    return redirect('/admin-registered-users')

def admin_events(request):
    event = Event.objects.all()
    context = {'event': event }
    return render(request, 'admin-events.html', context)

def admin_events_add(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            event = Event(
            event=data_record['event'],
            date=data_record['date'],
            time=data_record['time'],
            location=data_record['location'],
            contact=data_record['contact'],
            amount=data_record['amount'],
            seat=data_record['seat'],
            more=data_record['more'],
            image=fs.url(file_name),
            )
            event.save()
            messages.success(request, 'Event added successfully!')
            return redirect('/admin-events')
    context = {'form': form}
    return render(request, 'admin-events-add.html', context )

def admin_events_delete(request,id):
    Event.objects.filter(id=id).delete()
    messages.error(request, 'Event deleted!')
    return redirect('/admin-events')

def admin_instruments(request):
    itemadd = Itemadd.objects.all()
    context = {'instruments': itemadd }
    return render(request, 'admin-instruments.html', context )

def admin_instruments_add(request):
    form = InstrumentsForm()
    if request.method == 'POST':
        form = InstrumentsForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['main_photo']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            itemadd = Itemadd(
            name=data_record['name'],
            amount=data_record['amount'],
            available=data_record['avaliable'],
            image=fs.url(file_name),
            )
            itemadd.save()
            messages.success(request, 'Instruments added successfully!')
            return redirect('/admin-instruments')
    context = {'form': form}
    return render(request, 'admin-instruments-add.html', context )

def admin_instruments_delete(request,id):
    Itemadd.objects.filter(id=id).delete()
    messages.error(request, 'Instruments deleted!')
    return redirect('/admin-instruments')

def userprofile(request):
    context = { 'user' : User.objects.filter(username=request.session['username']) }
    return render(request, 'userprofile.html', context )

def buy(request):
    context = { 'itemadd' : Itemadd.objects.all() }
    return render(request, 'buy.html', context )

def music(request):
    context = { 'itemadd' : Itemadd.objects.all() }
    return render(request, 'music.html', context )

def events(request):
    context = { 'event' : Event.objects.all() }
    return render(request, 'events.html', context )

def logout(request):
    del request.session['is_logged_in']
    del request.session['username']
    return redirect('/login')

def contact_us(request):
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
            return redirect('/contact-us')
    context = {'form': form}
    return render(request, 'contact-us.html', context)

def admin_contactus(request):
    context = { 'contactus' : Contact_message.objects.filter() }
    return render(request, 'admin-contactus.html', context )

def admin_gallery(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['photos']
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)
            data_record = form.cleaned_data
            gallery = Gallery(
                photos=fs.url(file_name),
                text =data_record['text'],
            )
            gallery.save()
            messages.success(request, 'Image added successfully!')
            return redirect('/admin-gallery')
    context = {'form': form,'gallery': Gallery.objects.filter()}
    return render(request, 'admin-gallery.html', context )

def admin_delete(request,id, slug):
    if slug == 'gallery':
        Gallery.objects.filter(id=id).delete()
        messages.error(request, 'Image deleted!')
        return redirect('/admin-gallery')
    elif slug == 'contact':
        Contact_message.objects.filter(id=id).delete()
        messages.error(request, 'Messages deleted!')
        return redirect('/admin-cmessages')

def gallery(request):
    context = {'gallery': Gallery.objects.filter()}
    return render(request, 'gallery.html', context )
