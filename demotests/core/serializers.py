from rest_framework import serializers

from core.models import Content


class ContentSerializer(serializers.ModelSerializer):

    content_type_name = serializers.SerializerMethodField()
    gender_name = serializers.SerializerMethodField()
    goal_name = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = "__all__"
        lookup_field = "slug"

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "content_type_name",
            "gender_name",
            "goal_name",
        )

    def get_content_type_name(self, obj):
        return obj.get_content_type_display()

    def get_gender_name(self, obj):
        return obj.get_gender_display()

    def get_goal_name(self, obj):
        return obj.get_gender_display()
