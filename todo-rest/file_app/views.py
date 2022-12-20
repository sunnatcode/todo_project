from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.exceptions import APIException

from file_app.exception import FileNotFoundException
from file_app.models import File
from file_app.utils import upload_file, async_upload_file


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if "file" not in request.data:
            raise FileNotFoundException()
        file: File = upload_file(request.data['file'])
        response = {
            "message": {
                "file_id": file.id,
                "name": file.name,
                "content_type": file.content_type,
                "gen_name": file.gen_name,
                "size": file.size,
                'request_taken_tiem': 1
            },
            "status": status.HTTP_200_OK
        }
        return Response(response)

    def handle_exception(self, exc):
        return super().handle_exception(exc)


class AsyncFileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        if "file" not in request.data:
            raise FileNotFoundException()
        async_upload_file(request)
        return Response(status=status.HTTP_200_OK)

    def handle_exception(self, exc):
        return super().handle_exception(exc)
