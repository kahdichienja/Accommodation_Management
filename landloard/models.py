from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) 
    hostel_name = models.CharField(max_length=191)
    hostel_location = models.CharField(max_length=191, blank=True, null=True)
    your_full_name = models.CharField(max_length = 191, blank=True, null=True)
    your_phone_number = models.CharField(max_length = 191, blank=True, null=True)
    your_picture = models.ImageField(upload_to='landlord')
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.hostel_name} Hostel'

class HostelHomePage(models.Model):
    hostel_name = models.ForeignKey(LandlordProfile, on_delete = models.CASCADE)
    welcoming_message = models.TextField()
    background_image = models.ImageField(upload_to='hostel_homepages')

    def __str__(self):
        return f'{self.hostel_name} Home Page'

class HostelService(models.Model):
    hostel_name = models.ForeignKey(LandlordProfile, on_delete = models.CASCADE)
    security = models.TextField()
    water_supply = models.TextField()
    power_supply = models.TextField()
    bed_size = models.TextField()
    room_size = models.TextField()
    table_and_chair_availabitity = models.TextField()
    total_no_of_rooms = models.CharField(max_length=191, blank=True, null=True)

    def __str__(self):
        return f'{self.hostel_name} Services'

class HostelContact(models.Model):
    hostel_name = models.ForeignKey(LandlordProfile, on_delete = models.CASCADE)
    hostel_phone_number = models.CharField(max_length=20)
    hostel_mail = models.EmailField()
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    hostel_address = models.TextField()

    def __str__(self):
        return f'{self.hostel_name} Contact'

class HostelGallary(models.Model):
    hostel_name = models.ForeignKey(LandlordProfile, on_delete = models.CASCADE)
    photo_description = models.TextField()
    photo = models.ImageField(upload_to='Hostel_gallery')

    def __str__(self):
        return f'{self.hostel_name} Gallery'

class HostelPlan(models.Model):
    hostel_name = models.ForeignKey(LandlordProfile, on_delete = models.CASCADE)
    single_room_desc = models.TextField(blank=True, null=True)
    single_room_payment_price = models.CharField(max_length=12, blank=True, null=True)
    double_room_payment_price = models.CharField(max_length=12, blank=True, null=True)
    double_room_desc = models.TextField(blank=True, null=True)
    self_contained = models.TextField(blank=True, null=True)
    mpesa_shotcode = models.CharField(max_length=12, blank=True, null=True)
    self_contained_payment_price = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return f'{self.hostel_name} Plans'

