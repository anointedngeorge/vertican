from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings




def emailPlugin(mail_subject, from_head, from_email, template_name, obj, data):
    
    try:
        data = data
        mail_subject = mail_subject
        message = render_to_string(f"email_template/{template_name}.html", data)
        to_email = f"{obj.email}"
        email = EmailMessage(mail_subject, message, to=[to_email], from_email=f"{from_head} <{from_email}>")
        email.send()
    except Exception as e:
            return e