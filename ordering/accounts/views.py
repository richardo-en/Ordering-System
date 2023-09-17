from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateUserForm, CreateNewUser, GoodsForm, TypeForm, PlaceForm, TableForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import CustomUser, Goods, OrderPlace, OrderType, Tables
from .decorators import admin_required

#Home link
def home(request):
    user = request.user
    return render(request, 'accounts/home.html', {'user': user})

#Registration and login
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            if CustomUser.objects.filter(role=CustomUser.ADMIN).exists():
                return redirect('/')
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CreateUserForm()
        return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.user.role  == CustomUser.ADMIN:
                return redirect('/manage/admin/') 
            else:
                return redirect('/') 
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

#Admin panel
@admin_required
def admin_panel(request):
    return render(request, 'accounts/admin.html')

#Admin panel that manages users
@admin_required
def admin_users(request):
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/manage/admin/users")
    else:
        form = CreateNewUser()
        users = CustomUser.objects.filter(is_superuser=False)
        return render(request, 'accounts/users.html', {'users' : users, 'form': form})
    
@admin_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        form = CreateNewUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/users')
    else:
        form = CreateNewUser(instance=user)
        return render(request, 'accounts/edit_user.html', {'form': form, 'user': user})
    
@admin_required
def delete_user(request, user_id):
    if request.methof == "POST":
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return redirect('users')

#Admin panel that manages goods
@admin_required
def admin_goods(request):
    if request.method == "POST":
        form = GoodsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manage/admin/goods')
    else:
        goods = Goods.objects.all()
        form = GoodsForm()
        return render(request, 'accounts/goods.html', {'goods' : goods, 'form': form})
    
@admin_required
def edit_item(request, item_id):
    item = get_object_or_404(Goods, id=item_id)
    if request.method == 'POST':
        form = GoodsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/goods')
    else:
        form = GoodsForm(instance=item)
    return render(request, 'accounts/edit_item.html', {'form' : form, 'item': item})

@admin_required
def delete_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Goods, id=item_id)
        item.delete()
        return redirect('goods')

#Admin panel that manages tags
@admin_required
def admin_tags(request):
    if request.method == "GET":
        tags_type = OrderType.objects.all()
        tags_place = OrderPlace.objects.all()
        return render(request, 'accounts/admin_tags.html', {'tags_type' : tags_type, 'tags_place': tags_place})

#Order place
@admin_required
def order_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/tags/place/')
    else:
        tags = OrderPlace.objects.all()
        form = PlaceForm()
        return render(request, 'accounts/tags_place.html', {'tags_place' : tags, 'form': form})

@admin_required
def edit_place(request, tag_id):
    place = get_object_or_404(OrderPlace, id=tag_id)
    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/tags')
    else:
        form = PlaceForm(instance=place)
    return render(request, 'accounts/edit_tag.html', {'form' : form, 'tag': place})

@admin_required
def delete_place(request, tag_id):
    if request.method == "POST":
        place = get_object_or_404(OrderPlace, id=tag_id)
        place.delete()
        return redirect('tags')
    
@admin_required
def order_type(request):
    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/tags/type/')
    else:
        tags = OrderType.objects.all()
        form = TypeForm()
        return render(request, 'accounts/tags_type.html', {'tags_type' : tags, 'form': form})

@admin_required
def edit_type(request, tag_id):
    type = get_object_or_404(OrderType, id=tag_id)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/tags')
    else:
        form = TypeForm(instance=type)
    return render(request, 'accounts/edit_tag.html', {'form' : form, 'tag': type})

@admin_required
def delete_type(request, tag_id):
    if request.method == "POST":
        type = get_object_or_404(OrderType, id=tag_id)
        type.delete()
        return redirect('tags')
    
#Admin tables
@admin_required
def admin_tables(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/tables/')
    else:
        tables = Tables.objects.all()
        form = TableForm()
        return render(request, 'accounts/tables.html', {'tables' : tables, 'form': form})

@admin_required
def edit_table(request, table_id):
    table = get_object_or_404(Tables, id=table_id)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
        return redirect('/manage/admin/tables/')
    else:
        form = TableForm(instance=table)
        return render(request, 'accounts/edit_table.html', {'form' : form, 'table': table})

@admin_required
def delete_table(request, table_id):
    if request.method == "POST":
        table = get_object_or_404(Tables, id=table_id)
        table.delete()
        return redirect('/manage/admin/tables/')