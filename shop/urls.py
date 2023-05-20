from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.shop, name='shop'),
                  # path('<slug:model_slug>', views.shop_category, name='shop-products'),
                  # path('all', views.all_category, name='all-category'),
                  path('add-product', views.add_product, name='add-product'),
                  path('edit-product/<slug:prod_slug>', views.edit_product, name='edit-product'),
                  path('success', views.success, name='order-success'),
                  # path('<slug:category_slug>', views.product_category, name='product-category'),
                  path('<slug:category_slug>', views.shop_category, name='category'),

                  # path('sweetshirt', views.sweetshirt, name='sweetshirt'),
                  # path('cardigan', views.cardigan, name='cardigan'),
                  # path('hoody', views.hoody, name='hoody'),
                  path('<slug:category_slug>/<slug:prod_slug>', views.one_item, name='one-item'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
