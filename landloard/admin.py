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


admin.site.register(LandlordProfile)
admin.site.register(HostelService)
admin.site.register(HostelGallary)
admin.site.register(HostelContact)
admin.site.register(HostelPlan)