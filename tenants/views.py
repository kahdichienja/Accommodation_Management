from django.shortcuts import render
from landloard.models import LandlordProfile, HostelHomePage, HostelPlan, HostelService, HostelContact,HostelGallary

# Create your views here.

def home_hostels(request): 
    landlord_profile_qs = LandlordProfile.objects.all()

    return render(request, 'hostelpages/hostellistpage.html', {
        'landlord_profile_qs':landlord_profile_qs,
    })

def hostel_detailed_view(request, pk): 
    landlord_profile_qs = LandlordProfile.objects.filter(id = pk).get(id=pk)
    landlord_hostel_homepage_qs = HostelHomePage.objects.filter(hostel_name_id = pk)
    landlord_hostel_homepage_qs_first = HostelHomePage.objects.filter(hostel_name_id = pk).first()
    hostel_plan_qs = HostelPlan.objects.filter(hostel_name_id = pk)
    hostel_services_qs = HostelService.objects.filter(hostel_name_id = pk)
    hostel_contact_qs = HostelContact.objects.filter(hostel_name_id = pk)

    return render(request, 'hostelpages/hostel_view.html', {
        'landlord_profile_qs':landlord_profile_qs,
        'landlord_hostel_homepage_qs_first':landlord_hostel_homepage_qs_first,
        'landlord_hostel_homepage_qs': landlord_hostel_homepage_qs,
        'hostel_plan_qs': hostel_plan_qs,
        'hostel_services_qs': hostel_services_qs,
        'hostel_contact_qs': hostel_contact_qs,
    })

def hostel_detailed_view_gallery(request, pk): 
    landlord_profile_qs = LandlordProfile.objects.filter(id = pk).get(id=pk)
    landlord_hostel_gallery_qs_first = HostelGallary.objects.filter(hostel_name_id = pk).first()
    landlord_hostel_gallery_qs = HostelGallary.objects.filter(hostel_name_id = pk)

    return render(request, 'hostelpages/hostel_view_galley.html', {
        'landlord_profile_qs':landlord_profile_qs,
        'landlord_hostel_gallery_qs_first': landlord_hostel_gallery_qs_first,
        'landlord_hostel_gallery_qs':landlord_hostel_gallery_qs,
    })