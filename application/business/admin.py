from django.contrib import admin
from .models import Product,Order,Company,ItemList,Status
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Company)
admin.site.register(ItemList)
admin.site.register(Status)
