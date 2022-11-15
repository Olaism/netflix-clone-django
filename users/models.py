import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from subscriptions.models import SubscriptionPlan

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female')
)

AGE_BRACKETS = (
    ('kids', 'Kids'),
    ('adults', 'Adults')
)

class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField('Date Of Birth', null=True)
    age_bracket = models.CharField(
        max_length=6, 
        choices=AGE_BRACKETS,
        null=True
    )
    subscription_plan = models.ForeignKey(
        SubscriptionPlan, 
        on_delete=models.SET_NULL, 
        null=True
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', uuid=self.uuid)