from attr import fields
from movies.models import abc
from rest_framework import serializers

class movieserializers(serializers.ModelSerializer):
    class Meta:
        model = abc
        fields = '__all__'