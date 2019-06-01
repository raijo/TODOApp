from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("todo_title", "todo_content")

    # class Meta:
    #     fields = '__all__'

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
