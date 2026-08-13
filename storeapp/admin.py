from django.contrib import admin
from .models import Product, Cart, Wishlist, Order, SearchHistory, OrderTracking


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(SearchHistory)
admin.site.register(OrderTracking)