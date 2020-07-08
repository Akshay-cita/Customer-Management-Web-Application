from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm,CustomerForm


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

def OrderFormView(request):

    form= OrderForm()
    if request.method =='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context={'form':form}
    return render(request,'order_form.html',context)

def UpdateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    if request.method =='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context={'form':form}
    return render(request,'order_form.html',context)

def CreateCustomer(request):
    form=CustomerForm()
    if request.method == 'POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form}
    return render(request,'create_customer.html',context)

def DeleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    context={'item':order}
    return render(request,'delete_order.html',context)
