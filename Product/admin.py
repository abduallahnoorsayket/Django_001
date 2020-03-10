
from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'description', 'price', 'status', 'category', 'brand','image']

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product,ProductAdmin )


# Register your models here.
