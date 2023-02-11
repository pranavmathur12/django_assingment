
from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    #category = ServiceCategorySerializer()

    service = serializers.SerializerMethodField()

    def get_service(self, obj):
        return obj.service.upper() if obj.service else None