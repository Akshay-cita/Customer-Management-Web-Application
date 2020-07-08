from django.urls import path
from for_study_app1 import views

urlpatterns = [
path('cmr',views.initial_page,name='cmr'),
path('cmr/dashboard/',views.dashboard_view,name='dashboard'),
path('cmr/product/',views.product_view,name='product'),
path('cmr/customer/<str:pk>/',views.customer_view,name='customer'),
path('cmr/orderform/',views.OrderFormView,name='orderform'),
path('cmr/updateorder/<str:pk>/',views.UpdateOrder,name='orderupdate'),
path('cmr/createcustomer/',views.CreateCustomer,name='createcustomer'),
path('cmr/deleteorder/<str:pk>/',views.DeleteOrder,name='deleteorder'),




]
