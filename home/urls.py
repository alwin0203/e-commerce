from django.contrib import admin
from django.urls import path,include
from.import views
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('',views.index, name='home'),
    path('shop',views.shop, name='shopgrid'),
    path('product/<id>',views.product, name='single-product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('check_out/',views.check_out, name='check_out'),
    



    

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
