from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from auth_app.views import RegisterUser, MyTokenObtainPairView

urlpatterns = [
    # path('token/', LoginView.as_view(), name='token'),
    # path('kill-token/', LogoutView.as_view(), name='kill-token'),

    path("token/", TokenObtainPairView.as_view()),
    # path("token/", MyTokenObtainPairView.as_view()),
    path("refresh/token/", TokenRefreshView.as_view()),

    path('register/', RegisterUser.as_view(), name='register'),

]
