from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
import smtplib




# Create your views here.
def index(request):
    return render(request,"base/index.html")

def team(request):
    return render(request,"base/team.html")

def contact(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            gmail_user = 'akprogrammingclub@gmail.com'
            gmail_password = 'rfudlzffiuopesmk'

            sent_from = form.cleaned_data['from_email']
            to = ['akprogrammingclub@gmail.com']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            body = f"from: {sent_from}. message: {message}"

            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                messages.success(request,"email sent")
            except Exception as ex:
                messages.error(request,f"error: {ex}")
                
    return render(request, "base/contact.html", {'form': form})
