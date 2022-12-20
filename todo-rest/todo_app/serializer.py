from rest_framework import serializers

from todo_app.models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "done", "created_by"]


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description"]

    # def is_valid(self, raise_exception=False):
    #     self.data.get("title")
    #     return super().is_valid(raise_exception)
