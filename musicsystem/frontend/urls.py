from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('about-us', views.about_us, name='about-us'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('user-dashboard', views.user_dashboard, name='user-dashboard'),
    path('user-book-events', views.user_book_events, name='user-book-events'),
    path('user-book-instruments', views.user_book_instruments, name='user-book-instruments'),
    path('user-book-order-1/<int:item_id>/<slug:slug>', views.user_book_order_1, name='user-book-order-1'),
    path('user-book-order-2', views.user_book_order_2, name='user-book-order-2'),
    path('user-past-orders', views.user_past_orders, name='past-orders'),
    path('free-streaming', views.free_streaming, name='free-streaming'),
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('admin-registered-users', views.admin_registered_users, name='admin-registered-users'),
    path('admin-registered-users/delete/<int:user_id>', views.admin_registered_users_delete, name='admin-registered-users-delete'),
    path('admin-registered-users/status/<int:user_id>/<slug:slug>', views.admin_registered_users_status,
         name='admin-registered-users-status'),
    path('admin-events', views.admin_events, name='admin-events'),
    path('admin-events-add', views.admin_events_add, name='admin-events-add'),
    path('admin-events/delete/<int:id>', views.admin_events_delete, name='admin-events-delete'),
    path('admin-instruments', views.admin_instruments, name='admin-instruments'),
    path('admin-instruments-add', views.admin_instruments_add, name='admin-events-add'),
    path('admin-instruments/delete/<int:id>', views.admin_instruments_delete, name='admin-events-delete'),

    path('admin-cmessages', views.admin_contactus, name='admin-contactus'),
    path('admin-gallery', views.admin_gallery, name='admin-gallery'),
    path('admin-podcast', views.admin_podcast, name='admin-podcast'),
    path('admin-custom-delete/<int:id>/<slug:slug>', views.admin_delete, name='admin-delete'),

    path('userprofile', views.userprofile, name='userprofile'),
    path('buy', views.buy, name='buy'),
    path('music', views.music, name='music'),
    path('event', views.events, name='events'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)