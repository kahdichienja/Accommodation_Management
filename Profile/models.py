from django.db import models
from django.contrib.auth.models import User
from landloard.models import LandlordProfile, HostelPlan

# Create your models here.

class PaymentRequestHeaders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel_name = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length = 100)
    checkout_request_id = models.CharField(max_length = 100)
    response_description = models.CharField(max_length = 100)
    phone_number_used_for_payment = models.CharField(max_length = 100, blank=True)
    timestamp = models.DateTimeField(auto_now = True)


    def __str__(self):
        return  f'{self.hostel_name} request was {self.response_description}: checkout id = {self.checkout_request_id}' 


class TenantProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    your_full_name = models.CharField(max_length = 191, blank=True, null=True)
    phone_number = models.CharField(max_length = 191, blank=True, null=True)
    user_picture = models.ImageField(upload_to='tenant_profile')
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.your_full_name} : {self.phone_number} Profile'

class RoomateSelection(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_roomate = models.CharField(max_length=191)
    is_accepted = models.CharField(max_length=2, null=True, blank=True)

class HostelPaymentplan(models.Model):
    """Model definition for HostelPaymentplan. """

    # TODO: Define fields here
    tenant = models.ForeignKey(User, on_delete = models.CASCADE)
    paymentplan = models.ForeignKey(HostelPlan, on_delete=models.CASCADE)
    amountpaid = models.CharField(max_length=191)

    def __str__(self):
        """Unicode representation of HostelPaymentplan."""
        return f'{self.tenant} Payment Plan Is {self.amountpaid}'


class UserHostelPlan(models.Model):
    """Model definition for UserHostelPlan."""

    # TODO: Define fields here
    tenant = models.ForeignKey(User, on_delete = models.CASCADE)
    plan = models.ForeignKey(HostelPlan, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of UserHostelPlan."""
        return f'{self.plan} : {self.tenant} Plan'
    