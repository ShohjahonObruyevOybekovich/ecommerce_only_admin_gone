
from django.urls import path
from body.views import *
from custom_admin.views import *


urlpatterns = [
    path('product-menu-for-owner/', ProductListforOwnerAPIView.as_view(), name='product-owner-menu'),
    path('product-create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product-delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('product-owner-info/<int:pk>/',ProductownerinfoListAPIView.as_view(), name='product-owner-info'),

    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-products-list/<int:pk>/', CategoryProductsListAPIView.as_view(), name='category-products-list'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    path('subcategory-list/', SubCategoryListAPIView.as_view(), name='subcategory-list'),
    path('subcategory-create/', SubCategoryCreateAPIView.as_view(), name='subcategory-create'),
    path('subcategory-update/<int:pk>/', SubCategoryUpdateAPIView.as_view(), name='subcategory-update'),
    path('subcategory-delete/<int:pk>/', SubCategoryDeleteAPIView.as_view(), name='subcategory-delete'),
    path('subcategory-by-category/<int:pk>/',SubCategorybyCategoryListAPIView.as_view(), name='subcategory-by-category'),

    path('media-create/',MediaListCreateView.as_view(), name='media-create'),
    path('media-update/<int:pk>/', MediaUpdateAPIView.as_view(), name='media-update'),
    path('media-delete/<int:pk>/', MediaDeleteAPIView.as_view(), name='media-delete'),
    path('media-list/', MediaListAPIView.as_view(), name='media-list'),

    ]