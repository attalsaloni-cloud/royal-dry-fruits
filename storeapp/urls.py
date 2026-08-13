from django.urls import path

from .import views


urlpatterns=[

    path(
        "",
        views.home,
        name="home"
    ),


    path(
        "products/",
        views.products,
        name="products"
    ),


    path(
        "product/<int:id>/",
        views.product_detail,
        name="product_detail"
    ),


    path(
        "register/",
        views.register,
        name="register"
    ),


    path(
        "login/",
        views.user_login,
        name="login"
    ),


    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),


    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    path(
        "cart/add/<int:id>/",
        views.add_cart,
        name="add_cart"
    ),


    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    path(
    "cart/update/<int:id>/",
    views.update_cart,
    name="update_cart"
    ),

    path(
        "wishlist/add/<int:id>/",
        views.add_wishlist,
        name="add_wishlist"
    ),


    path(
        "wishlist/",
        views.wishlist,
        name="wishlist"
    ),


    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),


    path(
        "success/",
        views.success,
        name="success"
    ),


    path(
        "about/",
        views.about,
        name="about"
    ),


    path(
        "contact/",
        views.contact,
        name="contact"
    ),



path(
    'checkout/',
    views.checkout,
    name="checkout"
),


path(
    "track-order/",
    views.track_order,
    name="track_order"
),

path(
    "search-history/",
    views.search_history,
    name="search_history"
),



    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),


    path(
        'payment/<int:order_id>/',
        views.payment,
        name='payment'
    ),


    path(
        'success/',
        views.success,
        name='success'
    ),



]
