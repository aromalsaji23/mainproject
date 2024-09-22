"""Online_Grocery_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from grocery import views
from grocery.views import *
from django.conf.urls.static import static
from django.conf import settings
from grocery.views import sales_visualization




urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('weather/', get_weather, name='get_weather'),
    path('supplier/admin-requests/', view_admin_requests, name='view_admin_requests'),
path('update-request-status/', update_request_status, name='update_request_status'),
   path('delete-request/', delete_request, name='delete_request'),
   path('create_product_request/', views.create_product_request, name='create_product_request'),
   path('view_requests/', views.view_requests, name='view_requests'),
    path('supplier/request/details/', product_details, name='product_details'),
    path('supplier/admin-requests/', view_admin_requests, name='view_admin_requests'),
    path('create_product_request/', create_product_request, name='create_product_request'),
    path('product_request_list/', product_request_list, name='product_request_list'),
    path('respond_to_product_request/<int:request_id>/', respond_to_product_request, name='respond_to_product_request'),
    path('view-products/', view_products, name='view_products'),
    path('product_details/<int:product_id>/', product_details_view, name='product_details'),
    path('product_details/<int:product_id>/', product_details_view, name='product_details'),
    path('supplier/dashboard/', supplier_dashboard, name='supplier_dashboard'),
    path('register_supplier/', register_supplier, name='register_supplier'),
    path('login_supplier/', login_supplier, name='login_supplier'),
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('signup/', Signup, name="signup"),
	path('about/',About,name='about'),
	path('contact/',Contact,name='contact'),
    path('login/',Login,name="login"),
    path('logout/',Logout,name="logout"),
    path('view_user',View_user,name="view_user"),
    path('add_product',Add_Product,name="add_product"),
    path('view_feedback', View_feedback, name='view_feedback'),
    path('view_product/<int:pid>/', View_prodcut, name='view_product'),
    path('admin_view_product', Admin_View_product, name='admin_view_product'),
    path('login_admin',Admin_Login,name="login_admin"),
    path('admin_viewBooking', Admin_View_Booking, name='admin_viewBooking'),

    path('sales_report/', views.sales_report, name='sales_report'),
    path('sales-visualization/', sales_visualization, name='sales_visualization'),

    
    path('view_categary/', View_Categary, name='view_categary'),
    path('add_categary', Add_Categary, name='add_categary'),
     path('add_cart/<int:pid>/', Add_Cart, name='add_cart'),
    path('delete_product/<int:pid>/', delete_product, name='delete_product'),
    path('delete_user(?P<int:pid>)', delete_user, name='delete_user'),
    path('delete_feedback(?P<int:pid>)', delete_feedback, name='delete_feedback'),
    path('cart', view_cart, name='cart'),
    path('payment(?P<total>[0-9]+)', payment, name='payment'),
    path('delete_booking/(?P<str:pid>)/(?P<bid>[0-9]+)', delete_booking, name='delete_booking'),
    path('delete_admin_booking/(?P<str:pid>)/(?P<bid>[0-9]+)', delete_admin_booking, name='delete_admin_booking'),
    path('booking_detail/(?P<str:pid>)/(?P<bid>[0-9]+)', booking_detail, name='booking_detail'),
    path('admin_booking_detail/(?P<str:pid>)/(?P<bid>[0-9]+)/(?P<uid>[0-9]+)', admin_booking_detail, name='admin_booking_detail'),
    path('Edit_status/(?P<str:pid>)/(?P<bid>[0-9]+)', Edit_status, name='Edit_status'),
    path('remove_cart(?P<int:pid>)', remove_cart, name='remove_cart'),
    path('booking(?P<str:pid>)', Booking_order, name="booking"),
    path('view_booking', View_Booking, name='view_booking'),
    path('profile', profile, name='profile'),
    path('edit_profile', Edit_profile, name='edit_profile'),
    path('delete_category(?P<int:pid>)', delete_category, name='delete_category'),
    path('admin_home', Admin_Home, name='admin_home'),
    path('change_password', Change_Password, name="change_password"),
    path('send_feedback/(?P<pid>[0-9]+)', Feedback, name='send_feedback'),
    path('edit_category/<int:pid>',edit_category, name='edit_category'),
    path('edit_product/<int:pid>',edit_product, name='edit_product'),
    path('search_booking',search_booking, name='search_booking'),
    path('bookingbetweendate_reportdetails',bookingbetweendate_reportdetails, name='bookingbetweendate_reportdetails'),
    path('bookingbetweendate_report',bookingbetweendate_report, name='bookingbetweendate_report'),
    path('add-blog/', add_blog, name='add_blog'),
    path('my-blog/', view_my_blog, name='view_my_blog'),
    path('all-blogs/', view_all_blogs, name='view_all_blogs'),
    path('edit-blog/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', delete_blog, name='delete_blog'),

    path('create_pet_profile/', create_pet_profile, name='create_pet_profile'),
  
    path('edit_pet_profile/<int:pk>/', edit_pet_profile, name='edit_pet_profile'),
    path('view_pet_profile/<int:pk>/', view_pet_profile, name='view_pet_profile'),
     path('delete_pet_profile_confirm/<int:pk>/', delete_pet_profile_confirm, name='delete_pet_profile_confirm'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)