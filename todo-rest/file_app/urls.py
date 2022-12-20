from django.urls import path
from file_app.views import FileUploadView, AsyncFileUploadView

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="upload"),
    path("async-upload/", AsyncFileUploadView.as_view(), name="async_upload"),
]
