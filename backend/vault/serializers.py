from rest_framework import serializers
from vault.models import(
    APIPending,
    Category,
    API
)

class APICreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIPending
        fields = ['name', 'auth', 'category', 'cors', 'description', 'https', 'url', 'owner']
        read_only_fields = ['owner']


class APISerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = API
        fields = ('id', 'name', 'auth', 'category', 'cors', 'description', 'https', 'url', 'likes_count','liked_by_user')

    
    def get_liked_by_user(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id

        if user is not None:
            return obj.like_set.filter(user=user).exists()
        return False


class APICreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIPending
        fields = ['name', 'auth', 'category', 'cors', 'description', 'https', 'url']


class CategoryCountSerializer(serializers.ModelSerializer):
    api_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ['name', 'api_count']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
