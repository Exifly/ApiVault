from rest_framework import serializers
from vault.models import(
    Category,
    API
)

class APISerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = API
        fields = ('id', 'name', 'auth', 'category', 'cors', 'description', 'https', 'url')



class CategorySerializer(serializers.ModelSerializer):
    api_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ['name', 'api_count']
