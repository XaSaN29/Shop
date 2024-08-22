from django.contrib import admin
from apps.models import Product, Category, ProductImage, User, Wishlist

# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
# admin.site.register(User)
admin.site.register(Wishlist)

class ProductImageInlabe(admin.StackedInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name', 'price', 'quantity')
    inlines = [ProductImageInlabe, ]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'type')
    search_fields = ('username', 'type')


