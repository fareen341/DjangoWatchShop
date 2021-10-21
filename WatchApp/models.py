from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import ProtectedError
from django.http import JsonResponse


# from django.utils.text import slugify

#Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=30, help_text="Add watch color", verbose_name="Watch Color", unique=True)

    def __str__(self):
        return self.color

class Brand(models.Model):
    brand = models.CharField(max_length=30, help_text="Add watch brand", verbose_name="Watch Brand", unique=True)

    def __str__(self):
        return self.brand

class Size(models.Model):
    size = models.CharField(max_length=30, help_text="Add watch size", verbose_name="Watch Size", unique=True)

    def __str__(self):
        return self.size

class Product(models.Model):
    #related to product
    option= [
        ('male', 'Male'),
        ('female', 'Female'),
        ('band', 'Band'),
        ]
    option2= [
        ('no', 'No'),
        ('yes', 'Yes'),
        ]
    product_group_name=models.CharField(max_length=30, help_text="Note: The group name and product color should be unique", verbose_name="Product group name")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, help_text="If the color not available in the list, use the above color form to add color", verbose_name="Watch Color")
    # def colors_available(self):
    #     return ",".join([str(p) for p in self.color.all()])
    
    class Meta:
        unique_together = (('product_group_name', 'color'),)

    display_product=models.CharField(max_length=100, choices=option2, default="no",  help_text="If this is selected as yes the product will be visible on the product page, please select yes if you want this product to be display on product page", verbose_name="Display this product on product page?") 
    product_name = models.CharField(max_length=30, unique=True)
    regular_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField(null=True, blank=True)
    sale_last_date = models.DateField(null=True, blank=True, help_text="After the sale last date product will show the regular price")
    # sale_to = models.DateField()
    product_image = models.ImageField(upload_to = 'images', help_text="This is display image, it'll be visible on the product page", verbose_name="Display Image")
    product_img1 = models.ImageField(upload_to = 'images', help_text="Product's side image", verbose_name="Side Image")
    product_img2 = models.ImageField(upload_to = 'images', help_text="Product's side image", verbose_name="Side Image")
    product_img3 = models.ImageField(upload_to = 'images', help_text="Product's side image", verbose_name="Side Image")
    date = models.DateField(default=timezone.now())

    product_desc = models.TextField(max_length=200, verbose_name="Product Description") #textares
    size = models.ForeignKey(Size, on_delete=models.PROTECT, help_text="If the size not available in the list, use the above size form to add size", verbose_name="Watch Size")

    product_belongs = models.CharField(max_length=100, choices=option) 
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, help_text="If the brand not available in the list, use the above brand form to add brand", verbose_name="Watch Brand")

    # product_url = models.SlugField(unique=True)
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.product_name)
    #     super(Product, self).save(*args, **kwargs)
    #add slug field

    #related to inventary
    # stock_quantity = models.PositiveIntegerField(default=10)
    # limit = models.PositiveIntegerField(null=True, blank=True)
    # launcing_product = models.CharField(max_length=100, choices=option2, null=True, blank=True) 
    # sell_single = models.CharField(max_length=100, choices=option2, null=True, blank=True) #add default no here

    #related to shipping
    # weight_of_product = models.CharField(max_length=20)
  
    #related to home page
    featured_product = models.CharField(max_length=100, choices=option2, default='No', help_text="Select yes if you want this product to be displayed on featured product section", verbose_name="Featured product?")
    display_on_women_section = models.CharField(max_length=100, choices=option2, default='No', help_text="Select yes if you want this product to be displayed on women's menu section", verbose_name="Display on women's watches menu?")
    display_on_men_section = models.CharField(max_length=100, choices=option2, default='No', help_text="Select yes if you want this product to be displayed on men's menu section", verbose_name="Display on men's watches menu?")
    display_on_offer_section = models.CharField(max_length=100, choices=option2, default='No', help_text="If this product is on sale, select yes if you want this porduct to be display on the sale section", verbose_name="Display on sale selction?")
    # display_on_menu_section = models.CharField(max_length=100, choices=option2, null=True, blank=True, default='No')
  
    def __str__(self):
        return self.product_name

# class Related_products(models.Model):
#     #upselling
#     upselling_product = models.ManyToManyField(Product)
#     def all_products(self):
#         return ",".join([str(p) for p in self.upselling_product.all()])

# class Related_products_Cart(models.Model):
#     #downselling
#     # unique=models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart_product = models.ManyToManyField(Product)
#     def cart_products(self):
#         return ",".join([str(p) for p in self.cart_product.all()])



class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    prodobj = models.CharField(max_length=40)
    qnt = models.IntegerField(default=1)
    price = models.FloatField()
    img = models.ImageField()
    total = models.FloatField(default=0)
    class Meta:
        db_table = 'Cart'

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    msg = models.CharField(max_length=300)

class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    prodobj = models.CharField(max_length=40)
    qnt = models.IntegerField(default=1)
    price = models.FloatField()
    img = models.ImageField()
    total = models.FloatField(default=0)
    status = models.CharField(max_length=100)
    class Meta:
        db_table = 'Orders'

#make a custom validation that it should accept the original name can be different but nickname must be unique - seperated value with lower case only
'''
In this case all the watches of the same brand will be visible on the feature product on home page
to stop doing this ask seller make this product as featured product?
'''

class ShopCode(models.Model):
    unique_code = models.CharField(max_length=10)

@receiver(post_save, sender=Cart)
def endofsave(sender, instance, created, **kwargs):
    if created:
        instance.total=instance.qnt*instance.price
        instance.save()
