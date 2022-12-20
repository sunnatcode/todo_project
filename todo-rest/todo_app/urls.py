from django.urls import path
from todo_app.views import (
    TodoListView,
    TodoRetrieveView,
    TodoCreateAPIView)

urlpatterns = [
    path("", TodoListView.as_view()),
    path("retrieve/<int:pk>", TodoRetrieveView.as_view()),
    path("create/", TodoCreateAPIView.as_view()),
]
