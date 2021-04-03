from django.core.mail import message, send_mail
from django.shortcuts import render
from email_sender.settings import EMAIL_HOST_USER

from . import forms

# Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Django subscribe'
        message = 'Hope you are enjoying our website'
        recipients = str(sub['email'].value())
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            [recipients],
            fail_silently=False
        )
        return render(request, 'subscribe/success.html', {'recipients':recipients})
    return render(request, 'subscribe/index.html', {'form':sub})
