from django.urls import path

from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, admin_user_restore,admin_product_category_read

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-user-remove/<int:pk>/', UserDeleteView, name='admin_user_remove'),
    path('admin-user-restore/<int:user_id>/', admin_user_restore, name='admin_user_restore'),
    path('admin-product-category-read/', admin_product_category_read, name='admin_product_category_read'),

]
