from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Cart, Wishlist, Order 
from .models import SearchHistory, OrderTracking
from django import forms
from .models import (
    Product,
    Cart,
    Wishlist,
    Order,
    SearchHistory,
    OrderTracking
)
from .forms import CheckoutForm

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from django.contrib.auth.models import User

from .models import (
    Product,
    Cart,
    Wishlist,
    Order
)

from .forms import (
    RegisterForm,
    CheckoutForm
)



# Home Page

def home(request):

    products = Product.objects.all()

    return render(
        request,
        "home.html",
        {
            "products": products
        }
    )



# Product Page

def products(request):

    products = Product.objects.all()

    return render(
        request,
        "products.html",
        {
            "products": products
        }
    )
# Product Details

def product_detail(request,id):

    product = get_object_or_404(
        Product,
        id=id
    )


    return render(
        request,
        "product_detail.html",
        {
            "product":product
        }
    )



# Register

def register(request):

    if request.method=="POST":

        form = RegisterForm(request.POST)


        if form.is_valid():

            user=form.save(
                commit=False
            )

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            login(
                request,
                user
            )

            return redirect("home")


    else:

        form=RegisterForm()


    return render(
        request,
        "register.html",
        {
            "form":form
        }
    )



# Login

def user_login(request):

    if request.method=="POST":

        username=request.POST["username"]

        password=request.POST["password"]


        user=authenticate(
            username=username,
            password=password
        )


        if user:

            login(
                request,
                user
            )

            return redirect(
                "dashboard"
            )


    return render(
        request,
        "login.html"
    )



# Logout

def user_logout(request):

    logout(request)

    return redirect(
        "home"
    )



# Dashboard

def dashboard(request):

    return render(
        request,
        "dashboard.html"
    )



# Add Cart

def add_cart(request,id):

    product=get_object_or_404(
        Product,
        id=id
    )


    cart,created=Cart.objects.get_or_create(

        user=request.user,

        product=product
    )


    if not created:

        cart.quantity +=1

        cart.save()


    return redirect(
        "cart"
    )



# Cart Page

def cart(request):

    items=Cart.objects.filter(
        user=request.user
    )


    total=sum(
        item.total_price()
        for item in items
    )


    return render(
        request,
        "cart.html",
        {
            "items":items,
            "total":total
        }
    )



@login_required(login_url='login')
def update_cart(request, id):

    cart_item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )


    if request.method == "POST":

        quantity = int(
            request.POST.get("quantity")
        )

        cart_item.quantity = quantity

        cart_item.save()


    return redirect("cart")

# Wishlist Add
@login_required(login_url='login')
def add_wishlist(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )


    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )


    return redirect("wishlist")

# Wishlist Page
@login_required(login_url='login')
def wishlist(request):

    products = Wishlist.objects.filter(
        user=request.user
    )


    return render(
        request,
        "wishlist.html",
        {
            "products": products
        }
    )



@login_required(login_url='login')
def add_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart.quantity += 1
        cart.save()

    return redirect('cart')


# Checkout
def checkout(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )


    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity


    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user
            order.total = total
            order.status = "Pending"

            order.save()


            return redirect(
                'payment',
                order_id=order.id
            )


    else:

        form = CheckoutForm()



    context = {

        'form':form,

        'cart_items':cart_items,

        'total':total

    }


    return render(
        request,
        'checkout.html',
        context
    )



def track_order(request):

    orders = OrderTracking.objects.filter(
        order__user=request.user
    )

    return render(
        request,
        "track_order.html",
        {"orders":orders}
    )


def search_history(request):

    history = SearchHistory.objects.filter(
        user=request.user
    ).order_by("-searched_at")

    return render(
        request,
        "search_history.html",
        {"history":history}
    )



def search_product(request):
    query = request.GET.get("search")

    if query:
        SearchHistory.objects.create(
            user=request.user,
            keyword=query
        )

    products = Product.objects.filter(
        name__icontains=query
    )

    return render(
        request,
        "products.html",
        {"products": products}
    )



# About

def about(request):

    return render(
        request,
        "about.html"
    )



# Contact

def contact(request):

    return render(
        request,
        "contact.html"
    )


import razorpay
from django.conf import settings
from django.shortcuts import render

client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET
    )
)

def payment(request, order_id):

    order = Order.objects.get(
        id=order_id
    )


    if request.method == "POST":

        order.status = "Paid"

        order.save()


        Cart.objects.filter(
            user=request.user
        ).delete()


        return redirect(
            'success'
        )


    return render(
        request,
        'payment.html',
        {
            'order':order
        }
    )




def checkout(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )


    if request.method == "POST":

        address = request.POST.get("address")
        phone = request.POST.get("phone")


        if not address or not phone:
            return render(
                request,
                "checkout.html",
                {
                    "cart_items": cart_items,
                    "total": total,
                    "error": "Please enter address and phone number"
                }
            )


        order = Order.objects.create(
            user=request.user,
            total=total,
            address=address,
            phone=phone,
            status="Pending"
        )


        return redirect(
            "payment",
            order_id=order.id
        )


    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )
@login_required
def payment(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":

        order.payment_method = request.POST.get("payment_method")
        order.status = "Order Placed"
        order.save()

        Cart.objects.filter(user=request.user).delete()

        return redirect("success")

    return render(
        request,
        "payment.html",
        {
            "order": order
        }
    )



def success(request):

    return render(
        request,
        'success.html'
    )