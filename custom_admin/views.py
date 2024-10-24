# Create your views here.

# from rest_framework import generics
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
)
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from body.models import Product, Category, SubCategory, ProductMedia
from body.permissions import IsOwner
from body.serialize import *
from custom_admin.serialize import ProductownerinfoListSerializer, ProductCreateSerializer, ProductUpdateSerializer, \
    CategoryCreateSerializer, CategoryUpdateSerializer, CategoryListSerializer, SubCategoryListSerializer, \
    ProductListSerializer, User, MediaListSerializer


class ProductMenuAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # pagination_class = FlexiblePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']  # Specify the fields you want to filter on
    ordering_fields = ['price']
    search_fields = ['name']

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category = self.request.query_params.get('category')
    #     if category:
    #         queryset = queryset.filter(category=category)
    #     return queryset

class ProductByIDAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

    def get_object(self):
        try:
            obj = self.get_queryset().get(pk=self.kwargs.get('pk'))
            self.check_object_permissions(self.request, obj)
            return obj
        except Product.DoesNotExist:
            raise NotFound("Product not found.")


class ProductListforOwnerAPIView(ListAPIView):
    serializer_class = ProductownerinfoListSerializer
    # permission_classes = (IsAuthenticated, IsOwner)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['price']
    search_fields = ['name']

    def get_queryset(self):
        # Filter queryset based on the current authenticated user
        return Product.objects.filter(product_owner=super().get_queryset()
                                      .filter(product_owner=self.request.user))

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(product_owner=self.request.user)

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


 #fixx
class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj





class ProductownerinfoListAPIView(ListAPIView):
    serializer_class = ProductownerinfoListSerializer
    # permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        product_id = self.kwargs.get('pk')
        print(User.objects.filter(
            email__in=Product.objects.filter(id=product_id).values_list('product_owner__email', flat=True)))

        return User.objects.filter(
            email__in=Product.objects.filter(id=product_id).values_list('product_owner__email', flat=True)
        )
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']
    search_fields = ['name']

    def get_object(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class CategoryProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']  # Use filterset_fields for exact filtering

    def get_queryset(self):
        category_id = self.kwargs.get('pk') # Access pk from URL parameters
        return self.queryset.filter(category_id=category_id)



class SubCategoryCreateAPIView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    # permission_classes = (IsAuthenticated,IsOwner)
    # authentication_classes = (TokenAuthentication,)

class SubCategoryUpdateAPIView(UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

class SubCategoryDeleteAPIView(DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    permission_classes = (IsAuthenticated,IsOwner)
    authentication_classes = (TokenAuthentication,)
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    # permission_classes = (IsAuthenticated,IsOwner)
    # authentication_classes = (TokenAuthentication,)
    search_fields = ['name']
    django_filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']

class SubCategorybyCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    # permission_classes = (IsAuthenticated,IsOwner)
    # authentication_classes = (TokenAuthentication,)
    search_fields = ['name']
    django_filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']
    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return self.queryset.filter(category_id=category_id)


# from rest_framework import generics
# # from .models import Category, SubCategory, Product
# # from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
#
# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     search_fields = ['name']
#     django_filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
#
# class SubCategoryListCreateView(generics.ListCreateAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     search_fields = ['name']
#     django_filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
#
# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     search_fields = ['name']
#     django_filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

class MediaListCreateView(CreateAPIView):
    queryset = ProductMedia.objects.all()
    serializer_class = MediaListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# Update media
class MediaUpdateAPIView(UpdateAPIView):
    queryset = ProductMedia.objects.all()
    serializer_class = MediaListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# Delete media
class MediaDeleteAPIView(DestroyAPIView):
    queryset = ProductMedia.objects.all()
    serializer_class = MediaListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# List media with filtering
class MediaListAPIView(ListAPIView):
    queryset = ProductMedia.objects.all()
    serializer_class = MediaListSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['product_name']
    search_fields = ['product_name','file']
