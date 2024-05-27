import random
import string

from django.db import models

from doctranslation.modules.common.models import BaseModel


class DocumentQuerySet(models.QuerySet):
    def get_by_hex_id(self, hex_id):
        return self.filter(hex_id=hex_id).first()


class DocumentManager(models.Manager.from_queryset(DocumentQuerySet)):
    def create_document(self, name, location):
        hex_id = self._generate_unique_hex_id()
        return self.create(hex_id=hex_id, name=name, location=location)

    def generate_hex_id(self, length=16):
        characters = string.ascii_letters + string.digits
        hex_id = ''.join(random.choice(characters) for _ in range(length))
        return hex_id

    def _generate_unique_hex_id(self):
        while True:
            hex_id = self.generate_hex_id()
            if not Document.objects.filter(hex_id=hex_id).exists():
                return hex_id


class Document(BaseModel):
    hex_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    objects = DocumentManager()

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name
    
    def get_file(self):
        try:
            return open(self.location, 'rb')
        except Exception as e:
            pass

        return None