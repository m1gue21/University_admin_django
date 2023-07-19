from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.

def contact_form(request):
    return render(request, "contact.html")


def contact(request):
    if request.method == "POST":
        subject = request.POST["txtSubject"]
        message = request.POST["txtMessage"] + "/ Email: " + request.POST["txtEmail"]
        email_from = settings.EMAIL_HOST_USER
        email_to = ["xxxxxx@gmail.com"]
        send_mail(subject, message, email_from, email_to, fail_silently=False)
        return render(request, "success_contact.html")
    return render(request, "contact.html")
