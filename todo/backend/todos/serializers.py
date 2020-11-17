from rest_framework import serializers
from .models import Todo


# The serializers tranforms the data from the model into a JSON format
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body', )
