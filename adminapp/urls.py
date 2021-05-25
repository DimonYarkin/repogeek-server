from django.urls import path

from adminapp.views import index, UserListView, admin_users_create, admin_users_update, admin_user_remove, admin_user_restore,admin_product_category_read

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', admin_users_create, name='admin_users_create'),
    path('admin-users-update/<int:user_id>/', admin_users_update, name='admin_users_update'),
    path('admin-user-remove/<int:user_id>/', admin_user_remove, name='admin_user_remove'),
    path('admin-user-restore/<int:user_id>/', admin_user_restore, name='admin_user_restore'),
    path('admin-product-category-read/', admin_product_category_read, name='admin_product_category_read'),

]
