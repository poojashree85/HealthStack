from rest_framework import serializers
from .models import *

class dataserializer(serializers.ModelSerializer):
    Hospital_image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = hospitaldetails
        fields = "__all__"