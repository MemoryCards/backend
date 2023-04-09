from rest_framework import serializers
from .models import Card, Deck, Category, Tag, StudentProfile
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = slugify(instance.name)
        instance.updated_at = timezone.now()
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = slugify(instance.name)
        instance.updated_at = timezone.now()
        instance.save()
        return instance


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
                  'question',
                  'answer',
                  'deck'
                  ]


class DeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)
    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Deck
        fields = [
                  'id',
                  'name',
                  'description',
                  'created_by',
                  'tags',
                  'categories',
                  'cards'
                  ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
