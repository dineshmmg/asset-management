from django.core.mail import message
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, request
from cda_mailer.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
import pandas as pd
import time
# Create your views here.

def emails(request):
    form = RichContent(request.POST or None)
    
    if request.method == 'POST':
        e = pd.read_excel(request.FILES.get('email'))
        emails = e['email'].values
        length = len(emails)
        usernames = e['username'].values
        subject = request.POST.get('subject')
        content = request.POST.get('body')
        times = request.POST.get('time')
        count = 1
        for indx, email in enumerate(emails):
            username = usernames[indx]
            msg = EmailMultiAlternatives(subject, "<h4>Hi, "+username+"</h4><br>"+content, EMAIL_HOST_USER, [email])
            msg.content_subtype = "html"
            msg.send()
            print(count,"/",length)
            time.sleep(int(times))
            count += 1
        messages.success(request, 'Your mail has been sent successfuly!!!')
        return redirect('/')
    return render(request, "test.html", {'form':form})
