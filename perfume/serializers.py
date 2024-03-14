from rest_framework import serializers
from .models import Perfume, Designer, Note, Accord
from taggit.serializers import TagListSerializerField, TaggitSerializer


class PerfumeSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = tags = TagListSerializerField()

    # Specify model and fields
    class Meta:
        model = Perfume
        fields = (
            "name",
            "image",
            "designer",
            "summary",
            "tags",
            "top_notes",
            "heart_notes",
            "base_notes",
            "accords",
            "rating",
            "timestamp",
            "updated",
        )


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = ("name", "logo")


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("note", "image")


class AccordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accord
        fields = "__all__"
