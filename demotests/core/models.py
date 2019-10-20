import uuid

from django_extensions.db.fields import AutoSlugField

from django.db import models


class Content(models.Model):

    TYPE_CHOICES = (("cp", "Cupom"), ("cb", "Combo"), ("cm", "Communication"))

    GENDER_CHOICES = (("m", "Male"), ("f", "Female"))

    GOAL_CHOICES = (
        ("awar", "Awareness"),
        ("cons", "Consideration"),
        ("conv", "Conversion"),
    )

    name = models.CharField(unique=True, max_length=150)

    slug = AutoSlugField(populate_from="name", overwrite=True)

    tag = models.CharField(max_length=100)
    url = models.URLField()
    content_type = models.CharField(
        choices=TYPE_CHOICES, default="cb", max_length=2
    )
    gender = models.CharField(choices=GENDER_CHOICES, default="f", max_length=1)
    goal = models.CharField(choices=GOAL_CHOICES, default="awar", max_length=4)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
