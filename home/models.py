"""
This module defines the models for the 'home' app.
Models are classes that define the database blueprint for the app.
Each attribute of the class corresponds to a column in the database table for that model.
"""
from django.db import models


# models are classes in python
class User(models.Model):
    """
    User: This class defines the database blueprint for a user input in the 'home' app.
    Attributes:
    - name: The user's name, stored as a CharField with a maximum length of 200 characters.
    - birthdate: The user's birthdate, stored as a DateField.
    """
    def __str__(self):
        """
        This method returns the name of the user as a string.
        """
        return self.name

    name = models.CharField(max_length=200)
    birthdate = models.DateField()

    def birth_month_day(self):
        return self.birthdate.strftime('%m/%d')

    # choices set to a list of tuples
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to answer')
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Sign(models.Model):
    """
    Sign: This class defines the database blueprint for a specific astro type.
    Attributes:
    - name: The sign's name, stored as a CharField with a maximum length of 200 characters.
    - description: description of an astrology
    - url: image address related with a specific sign
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
