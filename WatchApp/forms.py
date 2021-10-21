from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from .models import Contact, Cart, Orders, ShopCode, Product, Color, Brand, Size



option= [
        ('male', 'Male'),
        ('female', 'Female'),
        ('band', 'Band'),
        ]
    
option2= [
        ('no', 'No'),
        ('yes', 'Yes'),
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['qnt']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopCode
        fields = '__all__'
    

class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets={
            'product_group_name':forms.TextInput(attrs={'class': 'myfieldclass'}),
            'product_desc':forms.Textarea(attrs={'class': 'editable', 'contenteditable':'true'}),
            'color':forms.Select(choices=option2),
            'sale_last_date':forms.DateInput(attrs={'type': 'date'})
        }
        # color = forms.MultipleChoiceField(
        # required=False,

        # widgets={
        # 'color':forms.CheckboxSelectMultiple(attrs={'class': 'selectpicker'}),
        # }      
        
        # choices=FAVORITE_COLORS_CHOICES,
    # )

class ColorDetailsForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'color':forms.TextInput(attrs={'class': 'myfieldclass'})
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'brand':forms.TextInput(attrs={'class': 'myfieldclass'})
        }
    
class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        widgets = {
            'size':forms.TextInput(attrs={'class': 'myfieldclass'})
        }

# class BookFilter(django_filters.FilterSet):
#     genre = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all())#widget=CheckboxSelectMultiple)
#     class Meta:
#         model = Color
#         fields = ['color']

# class BrandDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Brand
#         fields = '__all__'