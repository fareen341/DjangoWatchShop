from django.db.models.aggregates import Count
from django.shortcuts import render, HttpResponseRedirect
from django import contrib

from UserApp.models import UserProfile
from .models import Product, Brand, Color, Contact, Cart, Orders, ShopCode, Size
from .forms import ContactForm, ProductDetailsForm, ColorDetailsForm, CartForm, BrandForm, SizeForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.clickjacking import xframe_options_sameorigin
import datetime
from django.db.models import Sum
from WatchShop import settings
from django.core.mail import send_mail
from django.contrib import messages
from UserApp.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import JsonResponse



# Create your views here.


'''   
    uform = UserForm()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has correct credential
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            uform = UserForm()
    return render(request,'registration/login.html',{'uform':uform} )
'''

# def updateuser(request):
#     pass

# def updateuser(request):
#     currentuser =  request.user
#     print(currentuser)
#     data = User.objects.get(user=currentuser)
#     # data1 = User.objects.get(username=currentuser)
#     form = UserForm(request.POST, instance=data)
#     if request.method == 'POST':
#         print(request.POST)
#         # uform = UserForm(request.POST)  #if we dont pass instance it'll create new object
#         form = UserForm(request.POST, instance=data)
#         print(form)
#         if form.is_valid():
#             # print(uform, form)
#             # uobj=uform.save(commit=True)
#             # uobj.save()
#             # userobj = form.save(commit=False)
#             # userobj.user = uobj
#             form.save()
#             return redirect('/index/')
#     #     else:
#     #         form=UserProfileForm(request.POST, instance=data)
#     return render(request, 'hello.html',{'form':form})

    # if request.method == "POST":
    #     form = UserProfileForm(request.POST)
    #     if form.is_valid():
    #         # cl = form.cleaned_data['color']
    #         location = form.cleaned_data['location']
    #         contact = form.cleaned_data['contact']
    #         reg = UserProfile(location=location, contact=contact)
    #         reg.save()
    # else:
    #     form = UserProfileForm()
    # return render(request, 'account_detail.html', {'form':form}) #'brand_form':brand_form})

class ContactView(SuccessMessageMixin,CreateView):
    form_class = ContactForm
    # fields = "__all__"
    template_name = "contact.html"
    success_url = reverse_lazy('contact')
    success_message = "Your message submitted successfully!!"
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    all_brand=Brand.objects.all()[:4]

    # to pass context(brand, color, product) to mega menu
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context.update({'all_brand':self.all_brand, 'all_product':self.all_product, 'all_color':self.all_color})
        return context


# Create your views here.
# def baseview(request):
#     all=Product.objects.all()
#     return render(request, 'index.html',{'all':all})

def baseview(request, template_name):
    t=template_name
    all_brand=Brand.objects.all()[:4]
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    date=datetime.date.today()
    # for i in all_product:
    #     if i.product_belongs == "band":
    #         print('yes')
    #         band=i          #this will bring the last added product, so it is latest product, the image on the menu section will be the latest band
    #         print(band.brand)      
    #     else:
    #         print("no")
    # request.session['name']="anon_fareen"
    return render(request, t ,{'all_brand':all_brand, 'all_product':all_product, 'all_color':all_color, 'date':date})#, 'band':band})

# def branddetail(request):
    
#     return render(request, 'base.html')


def about(request):
    x=request.user.is_active()
    return render(request, 'about.html',{'x':x})

# def contact(request):
#     return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def shop(request):
    all_product=Product.objects.all()
    date=datetime.date.today()
    return render(request, 'shop.html', {"all_product":all_product, "date":date})

def demo(request):
    return render(request, 'thanks.html')

# def add_product(request):
#     form = ProductDetailsForm()
#     return render(request, 'add_product.html', {'form':form})

class ProductView(SuccessMessageMixin,CreateView):
    form_class = ProductDetailsForm
    template_name = "add_product.html"
    success_url = reverse_lazy('addproducts')
    success_message = "Product Added!!"
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    all_brand=Brand.objects.all()[:4]

    # to pass context(brand, color, product) to mega menu
    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context.update({'all_brand':self.all_brand, 'all_product':self.all_product, 'all_color':self.all_color})
        return context


@xframe_options_sameorigin
def color(request, template_name):
    t=template_name
    #color form
    if request.method == "POST":
        color_form = ColorDetailsForm(request.POST)
        if color_form.is_valid():
            c = color_form.cleaned_data['color']
            reg = Color(color=c)
            reg.save()
            messages.success(request, 'Color added, refresh page to see it in the below list.')
    else:
        color_form = ColorDetailsForm()
    
    #brand form
    if request.method == "POST":
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            b = brand_form.cleaned_data['brand']
            reg = Brand(brand=b)
            reg.save()
            messages.success(request, 'Brand added, refresh page to see it in the below list.')
    else:
        brand_form = BrandForm()

    #size form
    if request.method == "POST":
        size_form = SizeForm(request.POST)
        if size_form.is_valid():
            s = size_form.cleaned_data['size']
            reg = Size(size=s)
            reg.save()
            messages.success(request, 'Size added, refresh page to see it in the below list.')
    else:
        size_form = SizeForm()
    return render(request, t, {'color_form':color_form, 'brand_form':brand_form, 'size_form':size_form}) #'brand_form':brand_form})

def Commomview(request):
    color=Color.objects.all()
    brand=Brand.objects.all()
    size=Size.objects.all()
    return render(request, "color_list.html", {'color':color, 'brand':brand, 'size':size})

class ColorUpdateView(SuccessMessageMixin,UpdateView):
        model=Color
        template_name = 'update_color.html'
        form_class = ColorDetailsForm
        context_object_name = 'color'
        success_url = "/colorlist/" 
        success_message = "Color Updated Successfully!!"

def ColorDeleteView(request, id):
    try:
        if request.method=="POST":
            pi=Color.objects.get(id=id)
            pi.delete()
            messages.success(request, 'Color Deleted Successfully!!')
            return redirect('/colorlist/')
    except ProtectedError as v:
        print(v)
        # x=Product.objects.filter(color=Color.objects.filter(id=id)[0])
        return HttpResponse(f"<h1>Cannot delete {pi.color} color, product related to {pi.color} color exists, delete the product with this color and try again.</h1>")      
    return render(request,'color_confirm_delete.html')
    
class BrandUpdateView(SuccessMessageMixin,UpdateView):
    model=Brand
    template_name = 'update_brand.html'
    form_class = BrandForm
    context_object_name = 'brand'
    success_url = "/colorlist/" #reverse_lazy('contact')
    success_message = "Brand Updated Successfully!!"


def BrandDeleteView(request, id):
    try:
        if request.method=="POST":
            pi=Brand.objects.get(id=id)
            pi.delete()
            messages.success(request, 'Brand Deleted Successfully!!')
            return redirect('/colorlist/')
    except ProtectedError as v:
        return HttpResponse(f"<h1>Cannot delete {pi.brand} brand, product related to {pi.brand} brand exists, delete the product with this brand and try again.</h1>")      
    return render(request,'brand_confirm_delete.html')

class SizeUpdateView(SuccessMessageMixin,UpdateView):
    model=Size
    template_name = 'update_size.html'
    fields="__all__"
    context_object_name = 'size'
    success_url = "/colorlist/" #reverse_lazy('contact')
    success_message = "Size Updated Successfully!!"

def SizeDeleteView(request, id):
    try:
        if request.method=="POST":
            pi=Size.objects.get(id=id)
            pi.delete()
            messages.success(request, 'Size Deleted Successfully!!')
            return redirect('/colorlist/')
    except ProtectedError as v:
        return HttpResponse(f"<h1>Cannot delete {pi.size} size, product related to {pi.size} size exists, delete the product with this size and try again.</h1>")      
    return render(request,'size_confirm_delete.html')


def showproduct(request):
    data=Product.objects.all()
    print(data)
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    all_brand=Brand.objects.all()[:4]
    brands=Brand.objects.all()
    colors=Color.objects.all()
    sizes=Size.objects.all()
    date=datetime.date.today()
    print(date)
    p=['a','b','c','d']
    count=4
    # date2=datetime.date(2010,1,29)
    # print(date2)
    # x=date>date2
    # print(x)
    return render(request, 'product.html', {'data':data, 'all_brand':all_brand, 'all_product':all_product, 'all_color':all_color, 'date':date, 'brands':brands, 'p':p, 'count':count, "colors":colors, "sizes":sizes})
    

def singlepage(request):
    return render(request, 'single_product.html')

def imgproduct(request):
    data=Product.objects.all()[0]
    return render(request, 'demo.html', {'data':data})

def displayproduct(request, id):
    prod=Product.objects.get(id=id)
    br=prod.product_group_name
    print(br)
    brands=prod.brand
    print(brands)
    date=datetime.date.today()
    x=Product.objects.all()
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    all_brand=Brand.objects.all()[:4]
    # us=Related_products.objects.all()
    return render(request, 'single_product.html',{'prod':prod,'all_brand':all_brand, 'all_product':all_product, 'all_color':all_color,'x':x, 'br':br, 'brands':brands, 'date':date})# 'us':us})


# main function
def cartview(request, id):
    if request.user.is_anonymous:
        return redirect('/accounts/login/')
    else:
        prod=Product.objects.get(id=id)
        x=Product.objects.filter(id=id).exists()
        customer=request.user
        prodobj=prod.product_name
        date=datetime.date.today()
        if prod.sale_price != None and prod.sale_last_date >= date:
            price=prod.sale_price
        else:
            price=prod.regular_price
        img=prod.product_image
        Cart(customer=customer, prodobj=prodobj, price=price, img=img).save()

        # if prod.limit >= prod.stocak_quantity:
        #         print(request.user.email)
        #         subject="Stock Update"
        #         message=f"Your product {prod.product_name} is less than {prod.stocak_quantity} in the stock"
        #         email_from=settings.EMAIL_HOST_USER
        #         recipient_list = [request.user.email,]
        #         send_mail(subject, message, email_from, recipient_list)
        #         # return redirect('/index/')
        # else:
        #     print("do nothing")
        # s=prod.stocak_quantity
        # x=s-1
        # print(x)
        # Product.objects.filter(id=id).update(stocak_quantity=x)
        # print(prod.limit)
        return redirect('/mycarts/')
        # far=Cart.objects.all()
    # return render(request, 'practice.html',{'prod':prod,'pid':prodobj,'price':price, 'customer':customer, 'img':img})# 'us':us})


'''


def practice(request):
    data = serializers.serialize("json", Color.objects.all())
    request.session['cart']=data
    return render(request, "json.html", {'data':data})

def getsession(request):
    carts=request.session.get('cart')
    # print()
    return render(request, "json2.html", {'carts':carts})

#using session
def cartview(request, id):
    # request.session['cart']={}
    prod=Product.objects.get(id=id)
    
    if request.user.is_anonymous:
        product_document = {
                # 'pid':prod.id,
                'qnt':1
       }
        # request.session['cart']=product_document
        
        
        # request.session.set_default('cart', {})[str(product.id)] = product_document
        # request.session['cart'][str(prod.id)] = product_document
        # request.session.setdefault('cart', {})
        request.session.setdefault('cart', {})[prod.id] = product_document
        print("cart has:",request.session['cart'])
        request.session['price']=prod.regular_price
        request.session['img']=prod.product_image.url
        return redirect('/getsession/')
    else:
        customer=request.user
        prodobj=prod.product_name
        price=prod.regular_price
        img=prod.product_image
        Cart(customer=customer, prodobj=prodobj, price=price, img=img).save()
        return redirect('/showmycart/')

def getsession(request):
    p=Product.objects.all()
    l=[] 
    print(l)
    carts=request.session.get('cart')
    # x=list(map(carts.pid))
    # print(carts[0])
    for i in carts:
        x=int(i)
        l.append(x)
        if request.GET.get('i'):
                print("hello")
        else:
            print("nothing")

    # print("total cart:",carts)
    # print('pid',carts.get('17'))
    # for i in carts: 
    #     print('pid',carts.get(i))  
    #     j=int(i)
    #     l.append(j)
    #     # print("pid:",j.pid)
    # print("list:",l[0])
    return render(request, "getsession.html",{'carts':carts,'p':p,'l':l})#,'l':l, 'p':p})
'''


def showcartview(request):
    car = Cart.objects.filter(customer=request.user)
    print(car)
    # if Cart.objects.filter(pk=car.id).exists():
    # #     print('yes')
    # for i in car:
    #     # print(i.id)
    #     if Cart.objects.filter(pk=i.id).exists():
    #         print('yes exist')
    sub_total = Cart.objects.filter(customer=request.user)
    sum = sub_total.aggregate(Sum('total'))
    count=sub_total.aggregate(Sum('qnt'))
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    all_brand=Brand.objects.all()[:4]
    c=count['qnt__sum']
    if request.method=="POST":
        print("Post req",request.POST)
        q=request.POST['qnt']
        print(q)
        id=request.POST['id']
        x=Cart.objects.filter(id=id)
        for i in x:
            p=i.price
        x.update(qnt=q, total=int(q)*float(p))
        # print("total", total)
        # return JsonResponse({'response':True})
    return render(request, 'cartdetails.html', {'car':car,'sum':sum, 'c':c, 'all_product':all_product, 'all_color':all_color, 'all_brand':all_brand})


def updatecartv(request):
    if request.method=="POST":
        print("post rew:",request.POST)
        q=request.POST['qnt']
        x=Cart.objects.filter(id=id)
        y=x.price
        x.update(qnt=q*y)   
        print("hello")     
    # return JsonResponse({'response':True,'y':y,'x':x})
    return render(request,'practice.html')

def deletecart(request, id):
    if request.method=="POST":
        pi=Cart.objects.get(pk=id)
        print(pi)
        pi.delete()
        return redirect('mycarts')

# def updatecart(request):
    
#     if request.method=="POST":
#         print(request.POST)
#         q=request.POST['qnt']
#         x=Cart.objects.filter(id=id)
#         y=x.price
#         x.update(qnt=q*y)   
#         print("hello")     
#     # return JsonResponse({'response':True,'y':y,'x':x})
#     return render(request,'practice.html')


def practice(request):
    return render(request,'json.html')



class StudetUpdate(UpdateView):		#this will update the data
    model=Cart
    fields=['qnt']
    success_url = '/contact/'
    template_name = "practice2.html"
   
def update_data(request,id):
    car = Cart.objects.filter(customer=request.user)
    if request.method=="POST":
        pi=Cart.objects.get(pk=id)
        print(pi)
        fm=CartForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Cart.objects.get(pk=id)
        fm=CartForm(instance=pi)
    return render(request,'practice2.html', {'form':fm, 'car':car})


# def addtocart(request):
#     print("Cart item:",request.GET)
#     fid = request.GET['prodid']
#     price = request.GET['price']
#     customer = request.user
#     pobj = Product.objects.get(id=fid)
#     Cart(customer=customer, prodobj=pobj, price=price).save()
#     return redirect('/contact/')


#404 NOT FOUND PAGE CODE
# def handler404(request, *args, **argv):
#     response = render('404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


# def handler500(request, *args, **argv):
#     response = render('500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response

def sessioneg(request):
    request.session['name']='sonal'
    return render(request, "session.html")

def sendmail(request):
    print(request.user.email)
    subject="test"
    message="hello"
    email_from=settings.EMAIL_HOST_USER
    recipient_list = [request.user.email,]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('/contact/')

def filterview(request):
    prod=Product.objects.filter(product_belongs="female")
    print(prod)
    return render(request, "color_list1.html", {'prod':prod})


def addtocart(request):
    print("Cart item:",request.GET)
    fid = request.GET['prodid']
    price = request.GET['price']
    customer = request.user
    pobj = Product.objects.get(id=fid)
    Cart(customer=customer, prodobj=pobj, price=price).save()
    return redirect('/contact/')

def showcart(request):
    data = Cart.objects.filter(customer=request.user)
    c = Cart.objects.all()
    mylist=zip(data,c)
    print(c)
    all_brand=Brand.objects.all()[:4]
    all_product = Product.objects.all()
    all_color = Color.objects.all()[:4]
    return render(request, 'cartitem.html', {'mylist':mylist, 'c':c,'all_brand':all_brand, 'all_product':all_product, 'all_color':all_color})

def OrdersView(request):
    data = Cart.objects.filter(customer=request.user)
    print(data)
    for i in data:
        c=i.customer
        p=i.prodobj
        q=i.qnt
        pr=i.price
        img=i.img
        total=i.total
        status='pending'
        print(p)
        o=Orders.objects.create(customer=c,prodobj=p,qnt=q,price=pr,img=img,total=total,status=status)
        # i.delete()
    Cart.objects.all().delete()
    return render(request, "thanks.html",{'data':data})

def CustomerInfo(request):
    if request.method == "POST":
        color_form = UserProfileForm(request.POST)
        if color_form.is_valid():
            u = request.user
            c = color_form.cleaned_data['location']
            d = color_form.cleaned_data['contact']
            reg = UserProfile(user=u, location=c, contact=d)
            reg.save()
            messages.success(request, 'Color added, refresh page to see it in the below list.')
            return redirect('list')
    else:
        color_form = UserProfileForm()
    return render(request, 'address_confirmation.html', {'form':color_form})

class ProductListorders(ListView):
    model=Orders
    template_name = 'orders.html'
    context_object_name = 'orders'

    def get_object(self):
        return self.request.user

def practiceview(request):
    x=request.user.is_anonymous#request.session.session_key
    return render(request, 'practice.html', {'x':x})

class ProductListView(ListView):
    model=Product
    template_name = 'product_list.html'
    context_object_name = 'product'

class ProductUpdateView(SuccessMessageMixin,UpdateView):
    model=Product
    template_name = 'product_update.html'
    fields="__all__"
    context_object_name = 'product'
    success_url = "/productlist/" #reverse_lazy('contact')
    success_message = "Product Updated Successfully!!"

class ProductDeleteView(SuccessMessageMixin,DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = "/productlist/" 
    success_message = "Product Deleted Successfully!!"
    



    




    # request.session['name']="anon_fareen"
    # return render(request, t ,{'all_brand':all_brand, 'all_product':all_product, 'all_color':all_color})
    # def get_context_data(self, *args, **kwargs):
    #     context =super().get_context_data(*args, **kwargs)
    #     context['students'] = User.objects.all().order_by('name')
    #     return context

        

        
    # def save(self, commit=True):
    #     password = self.cleaned_data.get('password')
    #     user = super().save(commit=commit)
    #     if password:
    #         user.reset_password(password)
    #     else:
    #         pass
    #     return user
    
    # def get_form(self):         #copy same form for update
    #     form = super().get_form()
    #     # form.fields['name'].widget =forms.TextInput()
    #     # form.fields['password'].widget =forms.PasswordInput(render_value=True, attrs={'class':'myclass'})		#render_value=True for password to be visible 
    #     widgets={'password':forms.PasswordInput()}
    #     return widgets, form

# class StudentCreateView(CreateView):		#import create view first
#     form_class = UserForm
#     model = User
#     # fields = ['location','contact','username']

#     template_name = 'hello.html'


