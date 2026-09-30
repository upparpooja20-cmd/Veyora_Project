from django.contrib import admin
from django.urls import path

from store.views import (
    home,
    category,
    product,
    add_to_cart,
    cart,
    checkout,
    order_placed,
    wishlist
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('category/', category, name='category'),

    path('product/', product, name='product'),

    path('add-to-cart/', add_to_cart, name='add_to_cart'),

    path('cart/', cart, name='cart'),
    
    path('wishlist/', wishlist, name='wishlist'),

    path('checkout/', checkout, name='checkout'),

    path('order-placed/', order_placed, name='order_placed'),

]