from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category', 'price')
    search_fields = ('name', 'category', 'sub_category')
    readonly_fields = ()

    filter_horizontal = ()
    ordering = ('-price',)
    fieldsets = ()
    list_filter = ('category', 'sub_category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    search_fields = ('cat_name',)
    readonly_fields = ()

    filter_horizontal = ()
    ordering = ()
    fieldsets = ()
    list_filter = ()


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_cat_name', 'cat_name',)
    search_fields = ('cat_name', 'sub_cat_name')
    readonly_fields = ()

    filter_horizontal = ()
    ordering = ()
    fieldsets = ()
    list_filter = ('cat_name', 'sub_cat_name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(FeaturedCollection)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
