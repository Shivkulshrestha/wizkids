import os

from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render
from .models import Soochna, Photos, Admission, Download, Donations
from django.conf import settings


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST('name', '')
        email = request.POST('email', '')
        phone = request.POST('phone', '')
        desc = request.POST('desc', '')
        all_soochna = Soochna(name=name, email=email, phone=phone, desc=desc)
        all_soochna.save()
        # send mail
        message = Mail(
            from_email='rentoranywhere.info@gmail.com',
            to_emails='rentoranywhere.info@gmail.com',
            subject=name.capitalize() + ' just tried to contact',
            html_content='Email Id : ' + email + '\nPhone Number : ' + phone + '\nDescription : ' + desc)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
    return render(request, 'school/home.html')


def about(request):
    return render(request, 'school/about.html')


def contact(request):
    # here request.POST.get() function receives the data which is named as 'name' mentioned in the models.
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        all_soochna = Soochna(name=name, email=email, phone=phone, desc=desc)
        all_soochna.save()
        # send mail
        subject = name.capitalize() + ' just tried to contact'
        message = 'Email Id : ' + email + '\nPhone Number : ' + phone + '\nDescription : ' + desc
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
    return render(request, 'school/contact.html')


def admission(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name', '')
        admission_class = request.POST.get('admission_class', '')
        parents_name = request.POST.get('parents_name', '')
        phone_no = request.POST.get('phone_no', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        all_admission = Admission(student_name=student_name, admission_class=admission_class, parents_name=parents_name, phone_no=phone_no, email=email, address=address)
        all_admission.save()
        # send mail
        subject = 'New Admission Alert'
        message = 'Student Name : ' + student_name.capitalize() + '\nAdmission For Class : ' + admission_class + '\nParents Name : ' + parents_name.capitalize() + '\nPhone Number : '+'+91' + phone_no + '\nEmail Id : ' + email + '\nAddress : ' + address.capitalize()
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
    return render(request, 'school/admission.html')


def enquiry(request):
    return render(request, 'school/enquiry.html')


def gallery(request):
    photos = Photos.objects.all()
    return render(request, 'school/gallery.html', {'photos': photos})


def feesubmit(request):
    return render(request, 'school/feesubmit.html')


def download(request):
    down = Download.objects.order_by('-pub_date')
    return render(request, 'school/download.html', {'down': down})


def donation(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        don = Donations(name=name, email=email, phone=phone, desc=desc)
        don.save()
        # send mail
        subject = name.capitalize() + ' wanted to donate.'
        message = 'Email Id : ' + email + '\nPhone Number : ' + phone + '\nDescription : ' + desc
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
    return render(request, 'school/donation.html')


def test(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        all_soochna = Soochna(name=name, email=email, phone=phone, desc=desc)
        all_soochna.save()
        # send mail
        subject = name.capitalize() + ' just tried to contact'
        message = 'Email Id : ' + email + '\nPhone Number : ' + phone + '\nDescription : ' + desc
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
    return render(request, 'school/test.html')