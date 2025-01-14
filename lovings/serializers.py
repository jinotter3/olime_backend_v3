from rest_framework import serializers
from contents.serializers import TrackListSerializer, ContentListSerializer
from .models import Loving


class LovingSerializer(serializers.ModelSerializer):

    track = TrackListSerializer(
        many=True,
        read_only=True,
    )
    content = ContentListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Loving
        fields = (
            "pk",
            "name",
            "track",
            "content",
        )
