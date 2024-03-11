from django.urls import path
from .views import UserRegistrationView, VerifyOTP

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('allusers/', UserRegistrationView.as_view(), name='allusers'),
    path('userupdate/<int:pk>', UserRegistrationView.as_view(), name='user-update'),
    path('userdelete/<int:pk>', UserRegistrationView.as_view(), name='user-delete'),
    path('verify/', VerifyOTP.as_view(), name='user-verify'),
]
