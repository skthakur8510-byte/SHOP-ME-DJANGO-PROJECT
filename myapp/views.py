from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import categorys,product,mainimage,Carousel,Cart,CartItem
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
 
def image(request):
    if request.method=="POST":
        if mainimage.objects.count()>=1:
            messages.error(request,'ONLY ONE IMSGE ALLOW')
        img=request.FILES.get('img')
        sk=mainimage(img=img)
        sk.save()
        messages.success(request,'IMAGE UPLODE SUCCESSFULL')
    else:
        messages.error(request,'PLEASE UPLODE YOUR IMAGE CEARFULLY :')
    st=mainimage.objects.all()
   
    return render(request,"image.html",{"st":st})
    

def index(request):
    st=mainimage.objects.all()
    data={
        'st':st
    }
    return render(request,"index.html",data)
@login_required(login_url='/login')
def delete(request):
    id = request.GET.get("id")

    if not id:
        messages.error(request, "Invalid request: No ID found.")
        return redirect("/image")

    try:
        obj = mainimage.objects.get(id=id)
        obj.delete()
        messages.success(request, "🗑️ Image deleted successfully!")
    except mainimage.DoesNotExist:
        messages.error(request, "⚠️ Image not found or already deleted.")
    
    return redirect("/image")



# user login area------------------------------------------------------------

def signin(request):
    if request.method=="POST":
        username=request.POST.get("Name")
        password=request.POST.get("Password")
        auser=authenticate(username=username,password=password)
        if auser is not None:
            login(request,auser)
            # messages.success(request,'✅ LOGIN SUCCESSFULL')
            return redirect("/HOME")   
        else:
            messages.error(request,'ERROR:LOGIN CEARFULLY')

    return render(request,"login.html")



@login_required(login_url='/login')
def SINGOUT(request):
    logout(request)
    return redirect("/")



def signup(request):
    if request.method=="POST":
        username=request.POST.get("Name")
        password=request.POST.get("Password")
        conform_password=request.POST.get("conform_Password")
        if password!=conform_password:
            messages.error(request,"Enter Correct Password ")
        elif User.objects.filter(username=username).exists():
            messages.error(request,'USER ALLREDY SIGNUP')
        else:
            new_user=User.objects.create_user(username=username,password=password)
            new_user.save()
            messages.success(request,'✅ SIGNUP SUCCESSFULL')
            return redirect("/login")
    
    return render(request,'signup.html')

@login_required(login_url='/login')
def USER(request):
    if request.method=="POST":
       new_username=request.POST.get('NAME')
       if User.objects.filter(username=new_username).exists() and new_username != request.user.username:
           messages.error(request,"User Alredy Here")
       else:
           new_username!=request.user.username
           request.user.username=new_username
           request.user.save()
           messages.success(request,'✅ Successfull Update User Name')
       
       old_password=request.POST.get("old_password")
       new_password=request.POST.get("new_password")
       confirm_new_password=request.POST.get("confirm_new_password")
       if not old_password:
            messages.error(request, "❌ Please enter your old password to update username or password.")
            return redirect("/USER/")
       if old_password or new_password or confirm_new_password:
           user=request.user
           if not user.check_password(old_password):
               messages.error(request,"❌ Password Incorrect")
           elif new_password!=confirm_new_password:
               messages.error(request,"❌ Carefully Enter Password")
           else:
               user.set_password(new_password)
               user.save()
               update_session_auth_hash(request,user)
               messages.success(request,"✅ Profile Updated Successfull")
               return redirect("/USER/")

    return render(request,"user.html")




# category and product area------------------------------------------------


@login_required(login_url='/login')
def home(request):
    st=product.objects.all()
    if request.method == "POST":
        search = request.POST.get("serach")
        if search!=None:
            st=product.objects.filter(name__icontains=search)
    # pro=product.objects.filter(category__name="mens")
    # pro=product.objects.filter()
    carousel = Carousel.objects.all()
    data={
        # "pro":pro,
        "carousel":carousel,
        "st":st
    }
    return render(request,"home.html",data)

@login_required(login_url='/login')
def MENS(request):
    pro=product.objects.filter(category__name="mens")
    carousel = Carousel.objects.all()
    data={
        "pro":pro,
        "carousel":carousel
    }
    return render(request,"mens.html",data)




@login_required(login_url='/login')
def WOMENS(request):
    pro=product.objects.filter(category__name="Womens")
    carousel = Carousel.objects.all()
    data={
        "pro":pro,
        "carousel":carousel
    }
    
    return render(request,"womens.html",data)
@login_required(login_url='/login')
def KIDS(request):
    pro=product.objects.filter(category__name="kids")
    carousel = Carousel.objects.all()
    data={
        "pro":pro,
        "carousel":carousel
    }
    
    return render(request,"womens.html",data)



@login_required(login_url='/login')
def MORE(request, name):
    Product = get_object_or_404(product, name__iexact=name)
    more = product.objects.filter(name__iexact=name)
    mores = product.objects.exclude(id=Product.id)
    data={
        "more":more,
        "mores":mores,
        "product":Product
    }
    return render(request,'more.html',data)


@login_required(login_url='/login')
def SERVICE(request):
    return render(request,"service.html")


@login_required(login_url='/login')
def CONTACT(request):
    return render(request,"contact.html")





# ADD TO CART area------------------------------------------------
@login_required(login_url='/login')
def add_to_cart(request, id):
    
    pro = get_object_or_404(product, id=id)

    
    size = request.POST.get('size', 'ALL')
    quantity = int(request.POST.get('quantity', 1))

    
    cart, created = Cart.objects.get_or_create(user=request.user)

    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=pro,
        size=size
    )

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()

    
    messages.success(request, f"{pro.name} added to your cart successfully!")
    return redirect('view_cart')


@login_required(login_url='/login')
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


@login_required(login_url='/login')
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('view_cart')



# def update_quantity(request, item_id):
#     item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
#     if request.method == "POST":
#         new_quantity = int(request.POST.get('quantity', 1))
#         item.quantity = new_quantity
#         item.save()
#     return redirect('/view_cart')
@login_required(login_url='/login')
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == "POST":
        new_quantity = int(request.POST.get('quantity', 1))
        new_size = request.POST.get('size', item.size)

        existing_item = CartItem.objects.filter(
            cart=item.cart,
            product=item.product,
            size=new_size
        ).exclude(id=item.id).first()

        if existing_item:
            existing_item.quantity += new_quantity
            existing_item.save()
            item.delete()
        else:
            item.quantity = new_quantity
            item.size = new_size
            item.save()

    return redirect('view_cart')



@login_required(login_url='/login')
def payment(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'payment.html', {'total': total})




# ADD TO CART area------------------------------------------------

