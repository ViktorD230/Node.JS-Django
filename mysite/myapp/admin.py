from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ("name", )
    list_editable = ("price", "description")
    actions = ("make_zero", )


    def make_zero(self, request, queryset):
        queryset.update(price=0)



admin.site.register(Product, ProductAdmin)

admin.site.site_header = "My Django App"
admin.site.site_title = "Title od Django"
admin.site.index_title = "My admin"
