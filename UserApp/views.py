from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from WatchApp.models import ShopCode
from WatchApp.forms import ShopForm
from UserApp.models import UserProfile, Profile
from UserApp.forms import UserProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_sameorigin
from WatchApp.models import Orders
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#user registration and add the customer automatically in customer group
def userregister(request):
    # userform = UserForm()
    if request.method=="POST":
        userform=UserForm(request.POST)
        if userform.is_valid():
            user = userform.save()
            g=Group.objects.get(name="customer")
            user.groups.add(g)
            return redirect('login')
    else:
        userform=UserForm()
    return render(request, 'register.html', {'userform':userform})

#
def LoginView(request):
    form=AuthenticationForm()
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST.get('password')
        user=authenticate(username=uname, password=pwd)
        if user!=None and user.is_active:
            login(request, user)
            # print('USER:',user)
            # x=request.session.get('name',default="guest")
            # print("SESSION OBJECT:",x)
            return redirect('/')
        else:
            # msg="invalid username and password"
            return render(request, "registration/login.html",{'form':form})#, 'msg':msg})
    return render(request, "registration/login.html",{'form':form})

def CodeView(request):
    c = ShopCode.objects.all()[0].unique_code
    form = ShopForm()
    if request.method=="POST":
        code=request.POST['unique_code']
        if code == c:
            return redirect('/merchant_register/')
        else:
            msg="invalid code"
            return render(request, "registration/login.html",{'form':form, 'msg':msg})
    return render(request, "registration/login.html",{'form':form})

def merchantregister(request):
    # userform = UserForm()
    title="Create Business Account"
    if request.method=="POST":
        userform=UserForm(request.POST)
        if userform.is_valid():
            user = userform.save()
            g=Group.objects.get(name="seller")
            user.groups.add(g)
            return redirect('login')
    else:
        userform=UserForm()
    return render(request, 'register.html', {'userform':userform, 'title':title})

def LogoutView(request):
    logout(request)
    return redirect("/index")

@login_required(login_url='/accounts/login/')
def account(request):
    return render(request, 'account.html')

#userprofile functions start
@xframe_options_sameorigin
def dashboard(request, template_name):
    t=template_name
    ord=Orders.objects.filter(customer=request.user)
    if request.method == "POST":
        color_form = UserProfileForm(request.POST)
        if color_form.is_valid():
            u = request.user
            c = color_form.cleaned_data['location']
            d = color_form.cleaned_data['contact']
            reg = UserProfile(user=u, location=c, contact=d)
            reg.save()
            messages.success(request, 'Address and Contact details added successfully!!')
            return redirect('list')
    else:
        color_form = UserProfileForm() 
    x=UserProfile.objects.filter(user_id=request.user)
    print(x)
    return render(request, t, {'form':color_form,'ord':ord, 'x':x}) #'brand_form':brand_form})

class ProfileTemplate(TemplateView):
    template_name = 'registration/profile.html'

class UserListView(DetailView):
    model = UserProfile
    template_name = "user_address.html"

    def get_object(self):
        return self.request.user.userprofile

class UserUpdate(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'address.html'
    success_url = reverse_lazy('list')
    success_message = "Location updated"
    
    def get_object(self):
        return self.request.user.userprofile
#userprofile functions end       
      
#user functions start
class UserList(DetailView):
    model = User
    template_name = "account_detail.html"

    def get_object(self):
        return self.request.user
        
class UserUpdateView(SuccessMessageMixin,UpdateView):
    model = User#Profile
    # form_class = UserForm
    fields = ['username',  'first_name', 'last_name', 'email', ]
    template_name = 'userupdate.html'
    success_url = reverse_lazy('list')
    success_message = "details updated"

    def get_object(self):
        return self.request.user



