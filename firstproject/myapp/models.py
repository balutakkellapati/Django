from django.db import models
from phone_field import PhoneField
class Employee(models.Model):
	name = models.CharField(max_length=50, unique=False)

	def __str__(self):
		return self.name


class WorkHours(models.Model):
	name = models.ForeignKey("Employee",on_delete=models.PROTECT)
	days = models.DateField()
	hours = models.IntegerField()

	def __init__(self):
		return self.days


class Salary(models.Model):
	days = models.ForeignKey("WorkHours", on_delete=models.PROTECT)
	credited_salary = models.IntegerField()


class Login(models.Model):
	name = models.CharField(max_length=50, unique=False)
	email = models.EmailField()
	password = models.CharField(max_length=50, unique=False)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	GENDER_CHOICES = (
		('M', 'MALE'),
		('F', 'FEMALE'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)