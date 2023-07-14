from rest_framework import serializers
from .models import Project

class ProjecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','description', 'technology', 'created_at']