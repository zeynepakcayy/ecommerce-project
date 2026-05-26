from django.db import models

# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image =models.ImageField(upload_to='products/', blank=True)
    stock =models.IntegerField(default=0)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS =[
        ('pending', 'Bekliyor'),
        ('completed', 'Tamamlandı'),
    ]
    customer_name =models.CharField(max_length=200)
    customer_email =models.EmailField()
    created_at =models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=20, choices=STATUS, default='pending')

    def __str__(self):
        return f"{self.customer_name} - {self.created_at}"

class OrderItem(models.Model):
    order =models.ForeignKey(Order, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)
    price =models.DecimalField(max_digits=10, decimal_places=2)