import boto3

from .mixin import TranslationServiceMixin


class AmazonTranslateService(TranslationServiceMixin):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.client = boto3.client(
            'translate',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def translate_text(self, text, target_language=None):
        if not target_language:
            target_language = self.auto_detect_language(text)

        response = self.client.translate_text(
            Text=text,
            SourceLanguageCode='auto',  # Automatically detect the source language
            TargetLanguageCode=target_language
        )
        return response['TranslatedText']

    def detect_language(self, text):
        comprehend_client = boto3.client(
            'comprehend',
            aws_access_key_id=self.client._request_signer._credentials.access_key,
            aws_secret_access_key=self.client._request_signer._credentials.secret_key,
            region_name=self.client.meta.region_name
        )
        response = comprehend_client.detect_dominant_language(
            Text=text
        )
        return response['Languages'][0]['LanguageCode']
