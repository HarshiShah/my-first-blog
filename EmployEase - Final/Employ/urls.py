from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from rest_framework import routers

from Employ import classviews
from Employ.views import *
from . import views

urlpatterns = [
    url(r'^$',home_page),

    url(r'^MyJobs/(?P<pk>[0-9]+)$', login_required(classviews.MyJobsDetailsView.as_view()), name='myjobs_details'),
    url(r'^main/$',login_required(login_main),name="main"),
    url(r'^MyJobs$', login_required(classviews.JobsView.as_view()), name='myjobs'),
    url(r'^MyApplications$', login_required(classviews.ApplicationsView.as_view()), name='myapps'),
    url(r'^MyJobs/create$', login_required(classviews.JobCreateView.as_view()), name='myjobs_add'),
    url(r'^MyApplications/create$', login_required(classviews.ApplicationCreateView.as_view()), name='myapps_add'),
    url(r'^MyJobs/update/(?P<pk>[0-9]+)$', login_required(classviews.JobUpdateView.as_view())),
    url(r'^MyApplications/update/(?P<pk>[0-9]+)$', login_required(classviews.ApplicationUpdateView.as_view())),
    url(r'^MyJobs/delete/(?P<pk>[0-9]+)$', login_required(classviews.JobDeleteView.as_view())),
    url(r'^MyApplications/delete/(?P<pk>[0-9]+)$', login_required(classviews.ApplicationDeleteView.as_view())),
    url(r'^MyApplications/(?P<pk>[0-9]+)$', login_required(classviews.MyApplicationsDetailsView.as_view()), name='myapps_details'),
    url(r'^MyJobs/(?P<pk>[0-9]+)/create$', login_required(classviews.MyJobsDetailsCreateView.as_view()), name='myjobs_det_add'),
    url(r'^MyApplications/(?P<pk>[0-9]+)/create$', login_required(classviews.MyApplicationsDetailsCreateView.as_view()), name='myapps_det_add'),
    url(r'^MyJobs/(?P<pk>[0-9]+)/update$', login_required(classviews.MyJobsDetailsUpdateView.as_view())),
    url(r'^MyApplications/(?P<pk>[0-9]+)/update$', login_required(classviews.MyApplicationsDetailsUpdateView.as_view())),
    url(r'^AllJobs$', login_required(classviews.AllJobsView.as_view()), name='allJobs'),
    url(r'^AllApplications$', login_required(classviews.AllApplicationsView.as_view()), name='allApps'),
    url(r'^MyAccount$', login_required(views.my_account), name='allApps'),

    url(r'^AllApplications/(?P<pk>[0-9]+)$', login_required(classviews.AllApplicationsDetailsView.as_view()),name='allapps_details'),
    url(r'^AllJobs/(?P<pk>[0-9]+)$', login_required(classviews.AllJobsDetailsView.as_view())),
    url(r'^AllJobs/searchPIN$', login_required(views.searchJob_PIN), name='PIN_jobs'),
    url(r'^AllApplications/searchPIN$', login_required(views.searchApp_PIN), name='PIN_jobs'),
    url(r'^AllJobs/indexPIN$', login_required(views.index), name='PIN_jobs'),
    url(r'^AllApplications/indexPIN$', login_required(views.index), name='PIN_jobs'),
    url(r'^AllJobs/searchSkill$', login_required(views.searchJob_Skill), name='PIN_jobs'),
    url(r'^AllApplications/searchSkill$', login_required(views.searchApp_Skill), name='PIN_jobs'),
    url(r'^AllJobs/indexSkill$', login_required(views.skill_tag), name='PIN_jobs'),
    url(r'^AllApplications/indexSkill$', login_required(views.skill_tag), name='PIN_jobs'),
    url(r'^AllJobs/indexTime$', login_required(views.time_tag), name='PIN_jobs'),
    url(r'^AllApplications/indexTime$', login_required(views.time_tag), name='PIN_jobs'),
    url(r'^AllJobs/searchTime$', login_required(views.searchJob_Time), name='PIN_jobs'),
    url(r'^AllApplications/searchTime$', login_required(views.searchApp_Time), name='PIN_jobs'),
    url(r'^AllJobs/indexSalary$', login_required(views.salary_tag), name='PIN_jobs'),
    url(r'^AllJobs/indexQualification$', login_required(views.qualification_tag), name='PIN_jobs'),
    url(r'^AllApplications/indexQualification$', login_required(views.qualification_tag), name='PIN_jobs'),
    url(r'^AllJobs/searchSalary$', login_required(views.searchJob_Salary), name='PIN_jobs'),
    url(r'^AllJobs/searchQualification$', login_required(views.searchJob_Qualification), name='PIN_jobs'),
    url(r'^AllApplications/searchQualification$', login_required(views.searchApp_Qualification), name='PIN_jobs'),
    url(r'^sendMail/(?P<email_id>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$', login_required(views.sendMail)),
    url(r'^AllJobs/filters$', login_required(views.filter_Jobs), name='PIN_jobs'),
    url(r'^AllApplications/filters$', login_required(views.filter_Apps), name='PIN_jobs'),

]