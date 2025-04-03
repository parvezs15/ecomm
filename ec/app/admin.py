from django.contrib import admin
from .models import Product, Customer, Cart, OrderPlaced, Payment, Wishlist


# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount_price', 'category', 'product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'location', 'city', 'state', 'zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id',
                    'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']

from django.contrib import admin
from .models import Tutor

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subjects', 'charges_per_hour')  # Fields to display in the admin list view
    search_fields = ('name', 'email', 'subjects')  # Fields to search by
    list_filter = ('subjects',)  # Add filters for subjects


