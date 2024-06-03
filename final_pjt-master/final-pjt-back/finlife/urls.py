from django.urls import path
from . import views

app_name = 'finlife'
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('save-save-products/', views.save_save_products, name='save_save_products'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'),
    path('save-products/', views.save_products, name='save_products'),
    path('save-product-options/<str:fin_prdt_cd>/', views.save_product_options, name='save_product_options'),
    path('recommend/<int:user_id>/', views.recommend_products, name='recommend_products'),
    path('update/', views.update, name='update'),
]