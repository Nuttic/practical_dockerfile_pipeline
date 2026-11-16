from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'breed', 'age', 'is_cute', 'created_at']
        read_only_fields = ['id', 'created_at']
