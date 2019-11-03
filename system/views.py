from django.shortcuts import render
from landloard.models import LandlordProfile, HostelHomePage

# Create your views here.


def system_root_page(request):
    universities = LandlordProfile.objects.all()
    accommodation = HostelHomePage.objects.all()
    context={
        'universities': universities,
        'accommodation': accommodation,
    }
    return render(request, 'system_home.html', context)