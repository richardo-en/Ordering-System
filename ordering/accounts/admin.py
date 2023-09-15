from django.contrib import admin
from .models import CustomUser, OrderPlace, OrderType, Goods, TagColors

admin.site.register(CustomUser)
admin.site.register(OrderPlace)
admin.site.register(OrderType)
admin.site.register(Goods)
admin.site.register(TagColors)