from django.shortcuts import render
from authapp.models import User
from mainapp.models import ProductCategory,Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_read(request):
#     context = {'users':User.objects.all()}
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Регистрация прошла успешно!!!')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
#     else:
#         form = UserAdminRegisterForm()
#
#     context = {
#         'form': form
#     }

class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admin_staff:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, user_id):
#     selected_user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#
#     context = {
#         'form': form,
#         'selected_user': selected_user,
#     }
#     return render(request,'adminapp/admin-users-update-delete.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop Admin - Редактирование пользователя'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_remove(request, user_id):
#     user = User.objects.get(id=user_id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))

class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

class UserRestoreView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(success_url)


#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_restore(request, user_id):
#     user = User.objects.get(id=user_id)
#     user.is_active = True
#     user.save()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))

class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-product-category-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_category_read(request):
#     context = {'product_categorys':ProductCategory.objects.all()}
#     return render(request, 'adminapp/admin-product-category-read.html', context)
