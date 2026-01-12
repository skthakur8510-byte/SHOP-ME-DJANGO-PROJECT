from django.contrib import admin
from myapp.models import categorys,product,mainimage,Carousel,Cart,CartItem
# Register your models here.
class categorysAdmin(admin.ModelAdmin):
    list_display=("name",)
class productAdmin(admin.ModelAdmin):
    list_display=("name","description","price","category","img","size")
class mainimageAdmin(admin.ModelAdmin):
    list_display=['img']


admin.site.register(categorys,categorysAdmin)
admin.site.register(product,productAdmin)
admin.site.register(mainimage,mainimageAdmin)
admin.site.register(Carousel)
admin.site.register(Cart)
admin.site.register(CartItem)

