from django.contrib import admin
from .models import Color, Brand, Size, Product, Cart, Contact, Orders, ShopCode

# Register your models here.
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(ShopCode)