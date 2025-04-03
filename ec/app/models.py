from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATE_CHOICE = [
    ('Goa', 'Goa'),
    ('Delhi', 'Delhi')
]

CATEGORY_CHOICE = [
    ('CM', 'Computer'),
    ('DS', 'Data Science'),
    ('BD', 'Big Data'),
    ('AI', 'Artificial Intelligence'),
    ('BG', 'Big Data'),
    ('TU', 'Tutor'),
    ('SC', 'Schooling'),
    ('OT', 'Others')
]


class Product(models.Model):
    objects = None
    title = models.CharField(max_length=60, default='')
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Cart(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


class Customer(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
    ('Holding', 'Holding'),
)


class Payment(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


class Wishlist(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Teacher(models.Model):
    objects = None
    First_name = models.CharField(max_length=60)
    Last_name = models.CharField(max_length=60)
    Applying = models.CharField(max_length=60)
    Summary = models.TextField(max_length=4000)
    Email = models.EmailField()
    ContactNumber = models.CharField(max_length=60)
    CV = models.FileField(upload_to='cvs/')
    Photo = models.ImageField(upload_to='photos/')
    Id_upload = models.FileField(upload_to='ids/')

    def __str__(self):
        return self.name
class TeacherList(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    biography = models.TextField()
    subjects = models.CharField(max_length=255)  # Comma-separated subjects
    charges_per_hour = models.DecimalField(max_digits=6, decimal_places=2)  # e.g., 100.00
    profile_picture = models.ImageField(upload_to='teacher_profiles/', blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models


class Tutor(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    biography = models.TextField()
    subjects = models.CharField(max_length=255)  # Comma-separated subjects
    charges_per_hour = models.DecimalField(max_digits=6, decimal_places=2)  # e.g., 100.00
    profile_picture = models.ImageField(upload_to='tutor_profiles/', blank=True, null=True)

    def __str__(self):
        return self.name

