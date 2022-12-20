from django.shortcuts import render
from rest_framework import status
from .serializer import TodoCreateSerializer, TodoListSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo_app.models import Todo
from todo_app.serializer import TodoListSerializer, TodoCreateSerializer


class TodoListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer
    def get(self, request, *args, **kwargs):
        todos = Todo.active.filter(created_by_id=request.user.id).all()
        serializer = TodoListSerializer(todos, many=True)
        # if serializer.is_valid():
        return Response({
            "body": serializer.data,
            "total_size": todos.count(),
            "status": status.HTTP_200_OK
        })


class TodoRetrieveView(RetrieveAPIView):
    serializer_class = TodoListSerializer
    queryset = Todo.active.all()
    permission_classes = [IsAuthenticated]

    def handle_exception(self, exc):
        return super().handle_exception(exc)


class TodoCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoCreateSerializer
    def post(self, request, *args, **kwargs):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(created_by_id=request.user.id)
            return Response({
                "message": "Successfully created",
                "todo_id": instance.id,
                "status": status.HTTP_201_CREATED
            })
        return Response({
            "message": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })
