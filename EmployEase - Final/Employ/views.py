from django.contrib.auth import logout
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from django.core.mail import EmailMessage

# Create your views here.
from django.template import loader

import Employ
from Employ.models import *


def home_page(request):
    return render_to_response(
        'Employ/home.html',
    )

def login_main(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    template = loader.get_template("Employ/Main.html")
    result = template.render(Context({"userName": username}))
    return HttpResponse(result)

def index(request):
    return render(request, 'Employ/form.html')

def time_tag(request):
    return render(request, 'Employ/form_timing.html')

def qualification_tag(request):
    return render(request, 'Employ/form_qualification.html')

def salary_tag(request):
    return render(request, 'Employ/form_salary.html')

def sendMail(request,email_id):
    if request.method == 'POST':
        content = request.POST.get('message', None)
        try:
            html = ( email_id,content)
            email = EmailMessage('Employ-Ease', content, to=[email_id])
            email.send()
            return HttpResponse(html)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/mail.html')




def skill_tag(request):
    return render(request, 'Employ/skill_form.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/EmployEase')

def my_account(request):
    return render(request, 'Employ/my_acc.html')

def searchJob_PIN(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user=Employer.objects.filter(PIN=search_id)
            template = loader.get_template("Employ/AllJobs.html")
            result = template.render(Context({"jobs": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchApp_PIN(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user=Employee.objects.filter(PIN=search_id)
            template = loader.get_template("Employ/AllApps.html")
            result = template.render(Context({"app": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')


def searchJob_Skill(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user=Employer.objects.filter(job_profile__skill_set__contains=search_id)
            template = loader.get_template("Employ/AllJobs.html")
            result = template.render(Context({"jobs": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchApp_Skill(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user=Employee.objects.filter(employee_profile__skill_set__contains=search_id)
            template = loader.get_template("Employ/AllApps.html")
            result = template.render(Context({"app": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchJob_Time(request):
    if request.method == 'POST':
        search_id = request.POST.get('value', None)
        try:
            if(search_id=='ANYTIME'):
                user = Employer.objects.all()
            else:
                user=Employer.objects.filter(job_profile__preferred_time=search_id)
            template = loader.get_template("Employ/AllJobs.html")
            result = template.render(Context({"jobs": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchApp_Time(request):
    if request.method == 'POST':
        search_id = request.POST.get('value', None)
        try:
            if (search_id == 'ANYTIME'):
                user = Employee.objects.all()
            else:
                user=Employee.objects.filter(employee_profile__preferred_time=search_id)
            template = loader.get_template("Employ/AllApps.html")
            result = template.render(Context({"app": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchJob_Salary(request):
    if request.method == 'POST':
        min = request.POST.get('salary_from', None)
        max = request.POST.get('salary_to', None)

        try:
            user=Employer.objects.filter(job_profile__salary__range=[min,max])
            template = loader.get_template("Employ/AllJobs.html")
            result = template.render(Context({"jobs": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchJob_Qualification(request):
    if request.method == 'POST':
        search_id = request.POST.get('value', None)
        try:
            if(search_id=='None'):
                user = Employer.objects.all()
            else:
                user=Employer.objects.filter(job_profile__qualifications=search_id)
            template = loader.get_template("Employ/AllJobs.html")
            result = template.render(Context({"jobs": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def searchApp_Qualification(request):
    if request.method == 'POST':
        search_id = request.POST.get('value', None)
        try:
            if (search_id == 'None'):
                user = Employee.objects.all()
            else:
                user=Employee.objects.filter(employee_profile__qualifications=search_id)
            template = loader.get_template("Employ/AllApps.html")
            result = template.render(Context({"app": user}))
            return HttpResponse(result)
        except Employer.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'Employ/form.html')

def filter_Jobs(request):
    if request.method == 'POST':
        PIN_id=request.POST.get('textfield', None)
        qualification_id = request.POST.get('value', None)
        salary_from=request.POST.get('salary_from', None)
        salary_to=request.POST.get('salary_to', None)
        time=request.POST.get('time', None)
        skill=request.POST.get('skill',None)
        try:
            salary_from=int(salary_from)
            salary_to=salary_to(salary_to)
        except ValueError:
            return render(request, 'Employ/filter_job.html')
        if (PIN_id == 'None'):
                user = Employer.objects.all()
        else:
            user = Employer.objects.filter(PIN=PIN_id)

        if (qualification_id == 'None'):
                user = Employer.objects.all()
        else:
                user = Employer.objects.filter(job_profile__qualifications=qualification_id)

        template = loader.get_template("Employ/AllJobs.html")
        result = template.render(Context({"jobs": user}))
        return HttpResponse(result)

    else:
        return render(request, 'Employ/form.html')


def filter_Apps(request):
    return