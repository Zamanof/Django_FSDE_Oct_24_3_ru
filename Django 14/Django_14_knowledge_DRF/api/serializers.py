from rest_framework import serializers
from notes.models import Note, Tag, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )

    tags_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source='tags',
        many=True,
        required=False,
        write_only = True,
    )

    class Meta:
        model = Note
        fields = [
            'id',
            'author',
            'title',
            'content',
            'category',
            'category_id',
            'tags',
            'tags_ids',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']