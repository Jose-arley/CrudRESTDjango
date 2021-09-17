from rest_framework import serializers
from .models import Developers


class DevelopersSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    Language_Develop = serializers.CharField(max_length=200)
    Experience = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    years = serializers.IntegerField()
    class Meta:
        model = Developers
        fields = ('__all__')
