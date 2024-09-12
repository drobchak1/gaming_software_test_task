from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path(r'get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
