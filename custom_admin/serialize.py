from django.contrib.auth import get_user_model
from rest_framework import serializers

from body.models import Product, Category, ProductMedia, SubCategory

User = get_user_model()

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']
        read_only_fields = ['created_at']


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']
        read_only_fields = ['created_at']



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProductCreateSerializer(serializers.ModelSerializer):
    product_owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # payment = PaymentSerializer()

    class Meta:
        model = Product
        fields = ['name','nameRU',"infoUZ", "infoRU",'category','subcategory','photos_or_videos', 'price', 'propertiesUz',"propertiesRU",'product_owner']
        read_only_fields = ['created_at']

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','nameRU',"infoUZ", "infoRU",'category','subcategory','photos_or_videos', 'price', 'propertiesUz',"propertiesRU"]
        read_only_fields = ['created_at', 'product_owner']

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = '__all__'



#ex_owner field will delete couse of new incoming features like abilty to create a product permission for all user who want to be costumer!
class ProductListSerializer(serializers.ModelSerializer):
    photos_or_videos = ProductMediaSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','nameRU',"infoUZ", "infoRU",'category','subcategory','photos_or_videos', 'price', 'propertiesUz',"propertiesRU"]
        read_only_fields = ['created_at']

class ProductownerinfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','name','category','created_at']


class MediaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = ["id",'product_name','file']

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'type']
#
# class SubCategorySerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(
#         queryset=Category.objects.all(),
#         slug_field='name'  # Fetch category based on name in request
#     )
#
#     class Meta:
#         model = SubCategory
#         fields = ['id', 'name', 'category']
#
# class ProductSerializer(serializers.ModelSerializer):
#     # Use SlugRelatedField for easy lookup or creation
#     category = serializers.SlugRelatedField(
#         queryset=Category.objects.all(),
#         slug_field='name',
#         allow_null=True,
#         required=False
#     )
#     subcategory = serializers.SlugRelatedField(
#         queryset=SubCategory.objects.all(),
#         slug_field='name',
#         allow_null=True,
#         required=False
#     )
#
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'nameRU', 'category', 'subcategory', 'infoUZ', 'infoRU', 'price', 'propertiesUz', 'propertiesRU', 'photos_or_videos', 'product_owner', 'created_at', 'updated_at']
