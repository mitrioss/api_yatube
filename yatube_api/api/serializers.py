from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        # укажите поля, доступные только для чтения
        read_only_fields = ('author',)
        model = Post