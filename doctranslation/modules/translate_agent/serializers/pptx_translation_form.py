from rest_framework import serializers

from doctranslation.modules.translate_agent.constants import (
    ALLOW_TRANSLATION_FORM_ENGINE,
    ALLOW_TRANSLATION_LANGUAGES,
)


class PptxUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    engine = serializers.CharField(max_length=100)
    is_translate_image = serializers.BooleanField()
    target_language = serializers.CharField(max_length=10)
    source_language = serializers.CharField(max_length=10)


    def validate_file(self, value):
        if not value.name.endswith('.pptx'):
            raise serializers.ValidationError("Only .pptx files are allowed.")
        return value

    def validate_engine(self, value):
        if value not in ALLOW_TRANSLATION_FORM_ENGINE:
            raise serializers.ValidationError("Invalid translation engine.")
        return value
    
    def validate_target_language(self, value):
        if value not in ALLOW_TRANSLATION_LANGUAGES:
            raise serializers.ValidationError("Invalid target language.")
        return value
    
    def validate_source_language(self, value):
        if value not in ALLOW_TRANSLATION_LANGUAGES:
            raise serializers.ValidationError("Invalid source language.")
        return value