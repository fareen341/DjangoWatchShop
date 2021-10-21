"""WatchShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from WatchApp import views
from UserApp import views as vw
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    #base view
    path('index/',views.baseview,{'template_name':'index.html'}, name="index"),
    # path('contact/',views.baseview,{'template_name':'contact.html'}, name="contact"),
    path('about/',views.baseview,{'template_name':'about.html'}, name="about"),
    path('account/',views.baseview,{'template_name':'account.html'}, name="account"),
    path('shop/',views.baseview,{'template_name':'shop.html'}, name="shop"),
    path('product/', views.showproduct, name="product"),

    #Parent iframe
    # path('account/',vw.account, name="account"), 
    #iframe paths
    path('dashboard/',login_required(vw.dashboard),{'template_name':'dashboard.html'}, name="dashboard"), 
    path('orders/',login_required(vw.dashboard),{'template_name':'orders.html'}, name="orders"), 
    # path('bills/',vw.dashboard,{'template_name':'bills.html'}, name="bills"), 
    # path('address/',vw.dashboard,{'template_name':'address.html'}, name="address"), 
    path('account_detail/',login_required(vw.dashboard),{'template_name':'account_detail.html'}, name="account_detail"), 
    # path('logout/',vw.dashboard,{'template_name':'logout.html'}, name="logout"), 
    
    path('contact/',views.ContactView.as_view(), name="contact"), 
    

    #Parent iframe
    path('addproducts/',login_required(views.ProductView.as_view()), name="addproducts"),
    #iframe path
    path('color/',login_required(views.color),{'template_name':'color.html'}, name="color"),
    path('brand/',login_required(views.color),{'template_name':'brand.html'}, name="brand"), 
    path('size/',login_required(views.color),{'template_name':'size.html'}, name="size"),
    # path('sameproduct/',views.color,{'template_name':'same_product.html'}, name="sameproduct"),
    # path('cartproduct/',views.color,{'template_name':'cartproduct.html'}, name="cartproduct"),
    path('info/',login_required(views.color),{'template_name':'info.html'}, name="info"),
    #update product link
    path('product/<int:id>/', views.displayproduct),

    #related to user management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', vw.LoginView, name="login"),
    path('accounts/profile/', vw.ProfileTemplate.as_view(), name='profile'),
    path('logoutuser/',vw.LogoutView, name="logoutuser"),

    #list user details(location & contact)
    path('user_address/', login_required(vw.UserListView.as_view()), name="user_address"),

    #edit user detail(location and contact)
    path('edituser/', vw.UserUpdate.as_view(), name="edituser"),

    #list user details(username, password, email, firstname, lastname )
    path('list/', login_required(vw.UserList.as_view()), name="list"),

    #edit user detail(username, password, email, firstname, lastname )
    path('userupdate/', login_required(vw.UserUpdateView.as_view()), name="userupdate"),
    # path('mylocation/', vw.StudentCreate, name="mylocation"),

    # path('myaddress/', vw.AddressDetail, name="myaddress"),

    #for cart product display
    path('mycart/',login_required(views.showcart), name="mycart"),

    #add to cart view
    path('myorders/',login_required(views.ProductListorders.as_view()), name="myorders"),


    # path('addtocart/',vw.addtocart, name="addtocart"),



    #not required paths
    path('demo/',views.demo, name="demo"),
    # path('practice/',vw.practiceview, name="practice"),
    
    path('carts/<int:id>/',views.cartview, name="carts"),
    path('mycarts/',views.showcartview, name="mycarts"),
    path('delete/<int:id>/',views.deletecart, name="delete"),
    path('update/<int:pk>',views.StudetUpdate.as_view(), name="update"),

    path('myform/<int:id>', views.update_data, name="myform"),

    path('updatecart/',views.updatecartv, name="updatecart"),

    path('myorder/', views.OrdersView, name="myorder"),
    path('information/', views.CustomerInfo, name="information"),

    path('code/', vw.CodeView, name="code"),
    path('merchant_register/', vw.merchantregister, name="merchant_register"),
    path('register/', vw.userregister, name="register"),

    path('mail/', views.sendmail, name="mail"),
    path('filter/', views.filterview, name="filter"),
    path('productlist/', views.ProductListView.as_view(), name="productlist"),
    path('product_update/<int:pk>', views.ProductUpdateView.as_view(), name="product_update"),
    path('productdelete/<int:pk>', views.ProductDeleteView.as_view(), name="productdelete"),
    # path('colorlist/', views.ColorListView.as_view(), name="colorlist"),
    # path('colorlist/', views.BrandListView.as_view(), name="colorlist"),
    path('colorlist/', views.Commomview, name="colorlist"),
    path('update_color/<int:pk>', views.ColorUpdateView.as_view(), name="update_color"),
    path('colordelete/<int:id>', views.ColorDeleteView, name="colordelete"),

    path('update_brand/<int:pk>', views.BrandUpdateView.as_view(), name="update_brand"),
    path('branddelete/<int:id>', views.BrandDeleteView, name="branddelete"),

    path('update_size/<int:pk>', views.SizeUpdateView.as_view(), name="update_size"),
    path('sizedelete/<int:id>', views.SizeDeleteView, name="sizedelete"),



    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='change-password.html'), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='change-password-done.html'), name="password_change_done"),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name="password_reset"),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('json/', views.practice, name="json"),
    # path('json2/', views.getsession, name="json2"),
    #using session
    # path('session/', views.sessioneg, name="session"),
    # path('getsession/', views.getsession, name="getsession"),


    # path('single/',views.singlepage, name="single"), 
    # path('pic/', views.imgproduct, name="pic"),

    # path('update/product_url/', views.updateFoods),
    # path('student/int:pk',views.StudentDetailsViews.as_view(), name="student")
    # path('orders/',views.dashboard, name="orders"), 
    # path('profile/', views.ProfileTemplate.as_view(template_name="dashboard.html"), name='profile'),
    # path('brand/',views.branddetail, name="brand"),
    # RELATED TO USER MGMT

    # path('login/', auth_views.LoginView.as_view()),
    # path('editusers/', vw.updateuser, name="editusers"),

    # path('adduser/', vw.StudentCreateView.as_view(), name="adduser"),
    # path('/edituser/display/',vw.display,name="display")
    # path('cart/<int:pk>',views.mycartview, name="cart")


]

# handler404 = 'Watches.views.handler404'
# handler500 = 'Watches.views.handler500'
# handler404 = 'Watches.views.error_404'
# handler500 = 'Watches.views.error_500'
# handler403 = 'usermgmt.vw.error_403'
# handler400 = 'usermgmt.vw.error_400'

if settings.DEBUG:		
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


