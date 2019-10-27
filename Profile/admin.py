from django.contrib import admin
from Profile.models import  TenantProfile, PaymentRequestHeaders, RoomateSelection, UserHostelPlan, HostelPaymentplan

# Register your models here.

admin.site.register(HostelPaymentplan)

class TenantProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user","your_full_name", "phone_number", "user_picture"]
    list_display_links = ["user", "phone_number"]
    list_filter = ["user", "phone_number"]
    search_fields = ["user","phone_number"]
    class Meta:
        model = TenantProfile
admin.site.register(TenantProfile, TenantProfileModelAdmin)

class PaymentRequestHeadersModelAdmin(admin.ModelAdmin):
    list_display = ["user","hostel_name", "phone_number_used_for_payment", "merchant_request_id", "checkout_request_id", "response_description"]
    list_display_links = ["user", "phone_number_used_for_payment"]
    list_filter = ["user", "phone_number_used_for_payment"]
    search_fields = ["user","phone_number_used_for_payment"]
    class Meta:
        model = PaymentRequestHeaders
admin.site.register(PaymentRequestHeaders, PaymentRequestHeadersModelAdmin)

class RoomateSelectionModelAdmin(admin.ModelAdmin):
    list_display = ["user","user_roomate"]
    list_display_links = ["user"]
    list_filter = ["user"]
    search_fields = ["user","user_roomate"]
    class Meta:
        model = RoomateSelection
admin.site.register(RoomateSelection, RoomateSelectionModelAdmin)

class UserHostelPlanModelAdmin(admin.ModelAdmin):
    list_display = ["tenant","plan"]
    list_display_links = ["tenant"]
    list_filter = ["tenant"]
    search_fields = ["tenant","plan"]
    class Meta:
        model = UserHostelPlan
admin.site.register(UserHostelPlan, UserHostelPlanModelAdmin)
