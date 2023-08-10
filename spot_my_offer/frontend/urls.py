from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),

    path('site-admin', views.admin_login, name='admin'),
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('admin-shops', views.admin_shop, name='admin-shop'),
    path('admin-users', views.admin_users, name='admin-users'),
    path('admin-offers', views.admin_offers, name='admin-offers'),
    path('admin-places', views.admin_places, name='admin_places'),
    path('admin-contact-us', views.admin_contact_us, name='admin-contact-us'),
    path('admin-record-status/<int:id>/<slug:slug1>/<slug:slug2>',views.admin_record_status, name='admin_record_status' ),
    path('admin-record-delete/<int:id>/<slug:slug1>',views.admin_record_delete, name='admin_record_delete' ),
    path('user-login', views.user_login, name='user-login'),
    path('user-register', views.user_register, name='user-register'),
    path('user-dashboard', views.user_dashboard, name='dashboard'),
    path('user-offer', views.user_offer, name="user-offer"),
    path('users-offer-cart',views.user_offer_cart, name="users-offer-display"),
    path('user-offer-details/<int:id>', views.user_offer_details, name="user-offer"),
    path('user-offer-cart-payment/<int:id>/<int:discount_id>', views.user_offer_payment, name="user-offer-payment"),
    path('user-my-orders', views.user_my_orders, name='my_orders'),
    path('shop-login', views.shop_login, name='shop-login'),
    path('shop-register', views.shop_register, name='shop-register'),
    path('shop-dashboard', views.shop_dashboard, name='shop-dashboard'),
    path('shop-my-offers', views.shop_my_offers, name='shop-my-offers'),
    path('shop-profile', views.shop_profile, name='shop-profile'),
    path('shop-offer-delete/<int:id>', views.shop_offer_delete, name='shop-my-offers-delete'),
    path('shop-add-offer', views.shop_add_offers, name='shop-add-offers'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop-my-coupons', views.shop_my_coupons, name='shop-my-coupons'),
    path('shop-add-coupons', views.shop_add_coupons, name='shop-add-coupons'),
    path('shop-view-coupons/<int:id>', views.shop_view_coupons, name='shop-view-coupons'),
    path('shop-delete-coupons/<int:id>', views.shop_delete_coupons, name='shop-delete-coupons'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
