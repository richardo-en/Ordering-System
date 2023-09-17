from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'), #Login and register page
    path('', views.home, name='home'),#Home page
    path('manage/admin/', views.admin_panel, name='admin'),#Admin page
    path('manage/admin/goods/', views.admin_goods, name='goods'), #Goods page
    path('manage/admin/users/', views.admin_users, name='users'), #Users page
    path('manage/admin/tags/', views.admin_tags, name='tags'),#Tags page
    path('manage/admin/edit_user/<int:user_id>/', views.edit_user, name='edit_user'),  # Edit user page
    path('manage/admin/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('manage/admin/edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('manage/admin/delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('manage/admin/tags/place/', views.order_place, name='order_place'),
    path('manage/admin/tags/edit_place/<int:tag_id>/', views.edit_place, name='edit_place'),
    path('manage/admin/tags/place/delete/<int:tag_id>/', views.delete_place, name='delete_place'),
    path('manage/admin/tags/type/', views.order_type, name='tags_type'),
    path('manage/admin/tags/edit_type/<int:tag_id>/', views.edit_type, name='edit_type'),
    path('manage/admin/tags/type/delete/<int:tag_id>/', views.delete_type, name='delete_type'),
    path('manage/admin/tables/', views.admin_tables, name='tebles'),#
    path('manage/admin/edit_table/<int:table_id>/', views.edit_table, name='edit_table'),
    path('manage/admin/delete_table/<int:table_id>/', views.delete_table, name='delete_table'),#
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]