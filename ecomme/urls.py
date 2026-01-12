"""
URL configuration for ecomme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("image",views.image),
    path("login",views.signin),
    path("SINGOUT",views.SINGOUT,name='SINGOUT'),
    path("Register",views.signup,name='Register'),
    path("delete",views.delete),
    path("HOME/",views.home,name='HOME'),
    path("MENS/",views.MENS,name='MENS'),
    path("WOMENS/",views.WOMENS,name='WOMENS'),
    path("KIDS/",views.KIDS,name='KIDS'),
    path("MORE/<str:name>/",views.MORE,name='MORE'),
    path("SERVICE/",views.SERVICE,name='service'),
    path("CONTACT/",views.CONTACT,name='contact'),
    path("USER/",views.USER,name='USER'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:item_id>/', views.remove_item, name='remove_item'),
    path('update/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('payment/', views.payment, name='payment'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
