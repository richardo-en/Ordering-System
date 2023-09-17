from django.shortcuts import render, redirect
from .models import OverallOrder
from .forms import OverallOrderForm
from accounts.models import OrderPlace, Goods, Tables
import json

def orders_overview(request):
    orders = OverallOrder.objects.all()
    return render(request, "orders/order_overview.html" , {'orders' : orders})

def new_order(request):
    if request.method == "POST":
        form = OverallOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_overview')
    else:
        places = OrderPlace.objects.all()
        goods = Goods.objects.all()
        tables = Tables.objects.all()
        table_data = []
        for table in tables:
            number_list = list(range(1, table.number + 1))
            table_data.append({'table': table, 'number_list': number_list})
        places_data = [{"name": place.name} for place in places]
        goods_data = [{"name": good.name} for good in goods]
        form = OverallOrderForm()
        return render(request, "orders/new_order.html", {'form' : form, 'places_js': json.dumps(places_data), 'goods_js' : json.dumps(goods_data), 'places' : places, 'goods':goods, 'table_data': table_data})
