from django.db import models

# Create your models here.
class Category (models.Model):
    name= models.CharField(max_length=200)
    slug= models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    status = (
        ('Pending', 'PENDING'),
        ('Published', 'PUBLISHED'),
        ('Stock Out', 'STOCK OUT')
    )

    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    image = models.ImageField(default='default.png', null=True, blank=True, upload_to='product_images')
    description = models.TextField(max_length=800)
    status = models.CharField(max_length=10, choices=status)
    brand =models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name











