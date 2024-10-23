from django.contrib.auth import get_user_model
from rest_framework import serializers

from custom_admin.serialize import ProductListSerializer

User = get_user_model()
#
# class PurchaseHistorySerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#     product = ProductListSerializer()
#     total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
#
#     # Define a serializer method field to fetch product_amount
#     product_amount = serializers.SerializerMethodField()
#
#     class Meta:
#         model = PurchaseHistory
#         fields = ['product_amount', 'price', 'user', 'product', 'total_amount']
#         read_only_fields = ['created_at']
#
#     def get_product_amount(self, obj):
#         # Assuming PurchaseHistory has a ForeignKey to Savatcha and related_name is 'purchase_history'
#         savatcha_instance = obj.product.purchase_history.first()
#         if savatcha_instance:
#             serializer = SavatchaListSerializer(savatcha_instance)
#             return serializer.data['product_amount']
#         return None
#
#
# class LikedProductCreateSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     product_id = serializers.IntegerField()
#
#     class Meta:
#         model = liked
#         fields = ['user', 'product_id','uuid']  # Include 'user' and 'product'
#         read_only_fields = ['user','uuid']  # Make 'user' read-only
#
#
# class LikedProductListSerializer(serializers.ModelSerializer):
#     product = ProductListSerializer()
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#     class Meta:
#         model = liked
#         fields = '__all__'
#
#
#
# # class ProductLikedListSerializer(serializers.ModelSerializer):
# #     liked = LikedProductListSerializer(many=True, read_only=True)
# #     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
# #
# #     class Meta:
# #         model = Product
# #         fields = ['id', 'liked', 'user']
#
#
#
# class LikedUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
#
# class LikedProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = liked
#         fields = ['user', 'product', 'liked_status']
#
#
# class GetAppVersionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Versions
#         fields = '__all__'
#         read_only_fields = ['created_at']


from rest_framework import serializers
from .models import Category, SubCategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'  # Fetch category based on name in request
    )

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    # Use SlugRelatedField for easy lookup or creation
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )
    subcategory = serializers.SlugRelatedField(
        queryset=SubCategory.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'nameRU', 'category', 'subcategory', 'infoUZ', 'infoRU', 'price', 'propertiesUz', 'propertiesRU', 'photos_or_videos', 'product_owner', 'created_at', 'updated_at']