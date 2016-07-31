from __future__ import unicode_literals


# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIME=(
    ('MORNING','MORNING'),
    ('AFTERNOON','AFTERNOON'),
    ('EVENING','EVENING'),
    ('NIGHT','NIGHT'),
    ('ANYTIME','ANYTIME')
)

QUALIFICATIONS=(
    ('10th pass','10th pass'),
    ('12th pass','12th pass'),
    ('UG','Under Grdauate'),
    ('PG','Post Graduate'),
    ('NONE','None')
)



class Employee(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    PIN=models.IntegerField()
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.name



class Employee_Profile(models.Model):
    name = models.ForeignKey(Employee)
    description= models.CharField(max_length=300,null=True)
    birth_date=models.DateField()
    skill_set=models.CharField(max_length=500)
    preferred_time=models.CharField(max_length=15,choices=TIME)
    contact_number=models.BigIntegerField()
    emailID=models.EmailField()
    qualifications=models.CharField(max_length=10,choices=QUALIFICATIONS)
    def __str__(self):
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    PIN=models.IntegerField()
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.name

class Job_Profile(models.Model):
    name = models.ForeignKey(Employer,null=True)
    description= models.CharField(max_length=300,null=True)
    skill_set = models.CharField(max_length=500)
    preferred_time = models.CharField(max_length=15, choices=TIME)
    contact_number = models.BigIntegerField()
    emailID = models.EmailField()
    qualifications = models.CharField(max_length=10, choices=QUALIFICATIONS)
    salary=models.IntegerField(null=True)

    def __str__(self):
        return self.name

