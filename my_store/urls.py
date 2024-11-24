from django.urls import path
from my_store import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add-cat/', views.add_category, name='categoriy_add'),
    path('add-product/', views.add_product, name='add_product'),

    path('api/cart', views.view_cart, name='view_cart'),
    path('api/cart/add', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<str:product_id>', views.update_cart, name='update_cart'),
    path('cart/remove/<str:product_id>', views.remove_cart, name='remove_cart'),

    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),



]