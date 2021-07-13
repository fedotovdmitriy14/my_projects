from rest_framework import serializers
from .models import Craft


class CraftSerializer(serializers.ModelSerializer):              # валидация и преобразование данных в нужный формат
    class Meta:
        model = Craft
        # fields = ['__all__']
        fields = ['name', 'origin']