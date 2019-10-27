from django import forms
from django.contrib.auth.models import User
from .models import LandlordProfile, HostelHomePage, HostelContact, HostelService, HostelPlan, HostelGallary

class LandlordProfileForm(forms.ModelForm):
    class Meta:
        model = LandlordProfile
        fields = [ 
            'user',
            'hostel_name', 
            'hostel_location', 
            'your_full_name', 
            'your_phone_number', 
            'your_picture'
        ]

class HostelHompageForm(forms.ModelForm):
    
    welcoming_message = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_message', 'required' : 'true'}))
    
    class Meta:
        model = HostelHomePage
        fields = [
            'hostel_name',
            'welcoming_message',
            'background_image'
        ]

class HostelPlanForm(forms.ModelForm):
    
    single_room_desc = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_message', 'required' : 'true'}))
    double_room_desc = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_message', 'required' : 'true'}))
    self_contained = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_message', 'required' : 'true'}))
    
    class Meta:
        model = HostelPlan
        fields = [
            'hostel_name',
            'single_room_desc',
            'single_room_payment_price',
            'double_room_payment_price',
            'double_room_desc',
            'self_contained',
            'self_contained_payment_price',
            'mpesa_shotcode',
        ]
class HostelServiceForm(forms.ModelForm):
    """Form definition for HostelService."""
    security = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_messag', 'required' : 'true'}))
    table_and_chair_availabitity = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_message', 'required' : 'true'}))
    water_supply = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_messa', 'required' : 'true'}))
    power_supply = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcoming_mesage', 'required' : 'true'}))
    bed_size = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_welcomng_message', 'required' : 'true'}))
    room_size = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_wlcoming_message', 'required' : 'true'}))

    class Meta:
        """Meta definition for HostelServiceform."""

        model = HostelService
        fields = [
            'hostel_name',
            'security',
            'water_supply',
            'power_supply',
            'bed_size',
            'room_size',
            'table_and_chair_availabitity',
            'total_no_of_rooms',
        ]

class HostelContactForm(forms.ModelForm):
    """Form definition for HostelContact."""
    hostel_address = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_wlcoming_message', 'required' : 'true'}))

    class Meta:
        """Meta definition for HostelContactform."""

        model = HostelContact
        fields = [
            'hostel_name',
            'hostel_phone_number',
            'hostel_mail',
            'payment_method',
            'hostel_address',
        ]
class HostelGallaryForm(forms.ModelForm):
    """Form definition for HostelGallary."""
    photo_description = forms.CharField(widget = forms.Textarea(attrs={'class': 'materialize-textarea validate', 'id': 'id_wlcoming_message', 'required' : 'true'}))

    class Meta:
        """Meta definition for HostelGallaryform."""

        model = HostelGallary
        fields = ['hostel_name','photo_description','photo']

