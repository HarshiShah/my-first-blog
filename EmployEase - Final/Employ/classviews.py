
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from Employ.models import *


class JobsView(ListView):
    model=Employer
    template_name = "Employ/MyJobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        qs = Employer.objects.all()
        return qs.filter(created_by=self.request.user)

class ApplicationsView(ListView):
    model=Employee
    template_name = "Employ/MyApplications.html"
    context_object_name = "app"

    def get_queryset(self):
        qs = Employee.objects.all()
        return qs.filter(created_by=self.request.user)

class JobCreateView(CreateView):
    model = Employer
    template_name = "Employ/MyJobs_form.html"
    fields = ["name","description","PIN"]

    def get_success_url(self):
        return reverse('myjobs_det_add',args=(self.object.id,))

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(JobCreateView,self).form_valid(form)

    def get_queryset(self):
        qs = Employer.objects.all()
        return qs.filter(created_by=self.request.user)

class ApplicationCreateView(CreateView):
    model = Employee
    template_name = "Employ/MyApplications_form.html"
    fields = ["name","description","PIN"]

    def get_success_url(self):
        return reverse('myapps_det_add', args=(self.object.id,))

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ApplicationCreateView,self).form_valid(form)

    def get_queryset(self):
        qs = Employee.objects.all()
        return qs.filter(created_by=self.request.user)


class JobUpdateView(UpdateView):
    model = Employer
    template_name = "Employ/MyJobs_form2.html"
    fields = ["name","description","PIN"]

    def get_success_url(self):
        return reverse('myjobs')

    def get_queryset(self):
        qs = Employer.objects.all()
        return qs.filter(created_by=self.request.user)


class JobDeleteView(DeleteView):
    model = Employer
    template_name = "Employ/MyJobs_delete.html"

    def get_success_url(self):
        return reverse("myjobs")

    def get_queryset(self):
        qs = Employer.objects.all()
        return qs.filter(created_by=self.request.user)

class ApplicationUpdateView(UpdateView):
    model = Employee
    template_name = "Employ/MyApplications_form2.html"
    fields = ["name","description","PIN"]

    def get_success_url(self):
        return reverse('myapps')

    def get_queryset(self):
        qs = Employee.objects.all()
        return qs.filter(created_by=self.request.user)


class ApplicationDeleteView(DeleteView):
    model = Employee
    template_name = "Employ/MyApplication_delete.html"

    def get_success_url(self):
        return reverse("myapps")

    def get_queryset(self):
        qs = Employee.objects.all()
        return qs.filter(created_by=self.request.user)

class MyJobsDetailsView(DetailView):
    model=Job_Profile
    template_name = "Employ/MyJob_detail.html"
    context_object_name = "content"

    def get_queryset(self):
        qs = Job_Profile.objects.all()
        qs=qs.filter(name_id=self.kwargs['pk'])
        return qs


class MyJobsDetailsCreateView(CreateView):
    model=Job_Profile
    fields = '__all__'
    template_name = "Employ/MyJobDetail_form.html"

    def get_success_url(self):
        return reverse('myjobs')

class MyJobsDetailsUpdateView(UpdateView):
    model=Job_Profile
    fields = '__all__'
    template_name = "Employ/MyJobDetail_form.html"

    def get_queryset(self):
        qs= Job_Profile.objects.all()
        return qs.filter(name_id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('myjobs')


class MyApplicationsDetailsView(DetailView):
    model = Employee_Profile
    template_name = "Employ/MyApp_detail.html"
    context_object_name = "content"

    def get_queryset(self):
        qs = Employee_Profile.objects.all()
        qs = qs.filter(name_id=self.kwargs['pk'])
        return qs

class MyApplicationsDetailsCreateView(CreateView):
    model = Employee_Profile
    fields = '__all__'
    template_name = "Employ/MyJobDetail_form.html"


    def get_success_url(self):
        return reverse('myapps')


class MyApplicationsDetailsUpdateView(UpdateView):
    model = Employee_Profile
    fields = '__all__'
    template_name = "Employ/MyJobDetail_form.html"

    def get_queryset(self):
        qs = Employee_Profile.objects.all()
        return qs.filter(name_id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('myapps')


class AllJobsView(ListView):
    model=Employer
    template_name = "Employ/AllJobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        qs = Employer.objects.all()
        return qs

class AllJobsDetailsView(DetailView):
    model=Job_Profile
    template_name = "Employ/AllJobs_details.html"
    context_object_name = "content"

    def get_queryset(self):
        qs = Job_Profile.objects.all()
        qs=qs.filter(name_id=self.kwargs['pk'])
        return qs
class AllApplicationsView(ListView):
    model=Employee
    template_name = "Employ/AllApps.html"
    context_object_name = "app"

    def get_queryset(self):
        qs = Employee.objects.all()
        return qs

class AllApplicationsDetailsView(DetailView):
    model = Employee_Profile
    template_name = "Employ/AllApps_details.html"
    context_object_name = "content"

    def get_queryset(self):
        qs = Employee_Profile.objects.all()
        qs = qs.filter(name_id=self.kwargs['pk'])
        return qs

class PIN_JobDetails(ListView):
    model = Employer
    template_name = "Employ/AllJobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        if self.request.method=='POST':
            get_text = self.request.POST.get["textfield"]
            qs=Employer.objects.all()
            return qs

class PIN_ApplicationDetails(ListView):
    model = Employee
    template_name = "Employ/AllApps.html"
    context_object_name = "jobs"

    def get_queryset(self):
        if self.request.method=='POST':
            get_text = self.request.POST["textfield"]
            qs=Employee.objects.filter(PIN__exact=get_text)
            return qs