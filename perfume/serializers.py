from rest_framework import serializers
from .models import Perfume, Designer, Note, Accord
from taggit.serializers import TagListSerializerField, TaggitSerializer


class PerfumeSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    # Specify model and fields
    class Meta:
        model = Perfume
        fields = (
            "id",
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
        fields = ("id", "name", "logo")


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "note", "image")


class AccordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accord
        fields = ("id", "accord")
