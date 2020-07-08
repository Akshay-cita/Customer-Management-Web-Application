from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *



# Create your views here.

def initial_page(request):


    return render(request,'Base.html')

def dashboard_view(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()

    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    total_customers=customers.count()
    total_orders=orders.count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,'total_customers':total_customers,'delivered':delivered,'pending':pending}

    return render(request,'dashboard.html',context)

def product_view(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'product.html',context)


def customer_view(request,pk):
    customers=Customer.objects.get(id=pk)
    orders=customers.order_set.all()
    total_order=orders.count()

    context={'customers':customers,'orders':orders,'total_order':total_order}

    return render(request,'customer.html',context)
