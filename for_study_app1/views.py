from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import OrderForm,CustomerForm,CreateUserForm
from .filters import OrderFilter


# Create your views here.

def initial_page(request):
    return render(request,'Base.html')



def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,'username or password is incorrect')

        return render(request,'Login_page.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def UserPage(request):
    return render(request,'user.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form=CreateUserForm()


        if request.method == 'POST':
            form=CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created..'+ user)
                return redirect('login')
        context={'form':form}
        return render(request,'Reg_page.html',context)


@login_required(login_url='login')
def dashboard_view(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()

    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    total_customers=customers.count()
    total_orders=orders.count()

    context={'orders':orders,'customers':customers,'total_orders':total_orders,'total_customers':total_customers,'delivered':delivered,'pending':pending}

    return render(request,'dashboard.html',context)


@login_required(login_url='login')
def product_view(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'product.html',context)

@login_required(login_url='login')
def customer_view(request,pk):
    customers=Customer.objects.get(id=pk)
    orders=customers.order_set.all()
    total_order=orders.count()
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs
    context={'customers':customers,'orders':orders,'total_order':total_order,'myFilter':myFilter}
    return render(request,'customer.html',context)

@login_required(login_url='login')
def OrderFormView(request,pk):
    OrderFormSet= inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk)
    formset= OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method =='POST':
        formset= OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('dashboard')

    context={'formset':formset}
    return render(request,'order_form.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def CreateCustomer(request):
    form=CustomerForm()
    if request.method == 'POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form}
    return render(request,'create_customer.html',context)

@login_required(login_url='login')
def DeleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    context={'item':order}
    return render(request,'delete_order.html',context)
