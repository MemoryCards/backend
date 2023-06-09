from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


class TimestampAbstractModel(models.Model):
    """Abstract base class for models with created_at and updated_at fields."""
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class NameSlugAbstractModel(models.Model):
    """Abstract base class for models with name and slug fields."""
    name = models.CharField(max_length=255, unique=True, default='')
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(NameSlugAbstractModel, TimestampAbstractModel):
    pass


class Tag(NameSlugAbstractModel, TimestampAbstractModel):
    pass


class Deck(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='cards'
    )

    def __str__(self):
        return self.question[:50]


class StudentProfile(TimestampAbstractModel):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    chosen_decks = models.ManyToManyField(Deck)
    known_cards = models.ManyToManyField(Card)
