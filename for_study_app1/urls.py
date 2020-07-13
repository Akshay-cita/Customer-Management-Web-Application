from django.urls import path
from for_study_app1 import views

urlpatterns = [
path('cmr',views.initial_page,name='cmr'),
path('login/',views.login_page,name='login'),
path('user/',views.UserPage,name='user'),
path('logout/',views.logout_user,name='logout'),
path('register/',views.register_page,name='register'),
path('cmr/dashboard/',views.dashboard_view,name='dashboard'),
path('cmr/product/',views.product_view,name='product'),
path('cmr/customer/<str:pk>/',views.customer_view,name='customer'),
path('cmr/orderform/<str:pk>/',views.OrderFormView,name='orderform'),
path('cmr/updateorder/<str:pk>/',views.UpdateOrder,name='orderupdate'),
path('cmr/createcustomer/',views.CreateCustomer,name='createcustomer'),
path('cmr/deleteorder/<str:pk>/',views.DeleteOrder,name='deleteorder'),
]
