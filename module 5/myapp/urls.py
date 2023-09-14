from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('add_product',views.add_product,name='add_product'),
    path('add_detail',views.add_detail,name='add_detail'),
    path('view_product',views.view_product,name='view_product'),
    path('edit-product/<int:pk>',views.edit_product,name='edit-product'),
    path('delete-product/<int:pk>',views.delete_product,name='delete-product'),
]