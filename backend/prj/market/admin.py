from django.contrib import admin

from .models import Category, Product, Provider, Consumer, Store, OrderProduct, \
    Order


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('name',)
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(Provider, ProviderAdmin)


class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(Consumer, ConsumerAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('product', 'provider', 'price')
    search_fields = ('product__name', 'provider__name')
    fields = ('product', 'provider', 'price')
    list_filter = ('product__category',)


admin.site.register(Store, StoreAdmin)


class OrderProductInLIne(admin.TabularInline):
    """Форма для состава заказа"""
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'consumer', 'created_at')
    search_fields = ('consumer__name', 'created_at')
    list_filter = ('status',)
    inlines = (OrderProductInLIne,)


admin.site.register(Order, OrderAdmin)
