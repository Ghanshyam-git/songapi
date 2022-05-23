from  rest_framework import serializers
from mp3.models import *
class songserializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

