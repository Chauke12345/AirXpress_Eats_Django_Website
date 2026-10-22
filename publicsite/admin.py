from django.contrib import admin
from .models import PartnerShop
@admin.register(PartnerShop)
class PartnerShopAdmin(admin.ModelAdmin):
    list_display = ("name","is_active","app_featured","service_area","display_order")
    list_filter = ("is_active","app_featured")
    search_fields = ("name","description","food_categories","service_area")
    list_editable = ("is_active","app_featured","display_order")
