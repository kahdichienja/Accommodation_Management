from django.contrib import admin
from landloard.models import HostelHomePage, HostelService, HostelGallary, HostelContact, HostelPlan
from Profile.models import LandlordProfile

# Register your models here.
class HostelHomePageModelAdmin(admin.ModelAdmin):
    list_display = ["hostel_name","welcoming_message","background_image"]
    list_display_links = ["hostel_name"]
    list_filter = ["hostel_name"]
    search_fields = ["hostel_name","welcoming_message"]
    class Meta:
        model = HostelHomePage
admin.site.register(HostelHomePage, HostelHomePageModelAdmin)

class LandlordProfileModelAdmin(admin.ModelAdmin):
    list_display = ["hostel_name","user","your_phone_number"]
    list_display_links = ["hostel_name"]
    list_filter = ["hostel_name"]
    search_fields = ["hostel_name","user"]
    class Meta:
        model = LandlordProfile
admin.site.register(LandlordProfile, LandlordProfileModelAdmin)

admin.site.register(HostelService)
admin.site.register(HostelGallary)
admin.site.register(HostelContact)
admin.site.register(HostelPlan)