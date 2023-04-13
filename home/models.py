from django.db import models

# models are classes in python


# class User(models.Model):

#     def __str__(self):
#         return self.name

#     name = models.CharField(max_length=200)
#     birthdate = models.DateField()

#     def birth_month_day(self):
#         return self.birthdate.strftime('%m/%d')

#     # choices set to a list of tuples
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#         ('P', 'Prefer not to answer')
#     ]

#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Sign(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
