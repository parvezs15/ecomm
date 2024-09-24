from django.core.checks import messages
from django.db.models import Count
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import CustomerRegistrationForm, CustomerProfileForm
from .models import Product, Customer, Cart, Wishlist, OrderPlaced
from typing_extensions import ParamSpecKwargs
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/home.html", locals())


def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/about.html", locals())


def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/contact.html", locals())


class CategoryView(View):
    @staticmethod
    def get(request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())


class CategoryTitle(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/category.html", locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/productdetail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/customerregistration.html", locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, location=location, city=city, mobile=mobile,
                           state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/profile.html", locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, "app/address.html", locals())


class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "app/updateAddress.html", locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.location = form.cleaned_data['location']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    wishitem = 0
    for p in cart:
        value = p.quantity * p.product.discount_price
        amount = amount + value
    totalamount = amount + 40
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html', locals())

class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            user = request.user
            add = Customer.objects.filter(user=user)
            cart_items = Cart.objects.filter(user=user)
            famount = 0
            for p in cart_items:
                value = p.quantity * p.product.discount_price
                famount = famount + value
            totalamount = famount + 40
            razoramount = int(totalamount * 100)
#            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
#            data = {"amount": razoramount, "currency": "INR", "receipt": "order_rcptid_12"}
#            payment_response = client.order.create(data=data)
#           print(payment_response)
            return render(request, 'app/checkout.html', locals())

def orders(request):
        order_placed = OrderPlaced.objects.filter(user=request.user)
        return render(request, 'app/orders.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
            totalamount = amount + 40
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
            totalamount = amount + 40
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
            totalamount = amount + 40
            data = {
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)


def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data = {
            'message': 'Wishlist Added Successfully',
        }
        return JsonResponse(data)


def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data = {
            'message': 'Wishlist Remove Successfully',
        }
        return JsonResponse(data)


def search(request):
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html", locals())
