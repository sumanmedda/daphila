from django.core.mail import send_mail
from django.conf import settings
from .models import User

def send_email_to_client(otp,client_email):
    subject = "OTP"
    message = f"Please verify your account. Your otp is : {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [client_email]

    send_mail(subject, message, from_email, recipient_list)

    user_obj = User.objects.get(email=client_email)
    user_obj.otp = otp
    user_obj.save()
    