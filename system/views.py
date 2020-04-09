from django.shortcuts import render, redirect
from landloard.models import LandlordProfile, HostelHomePage

# Create your views here.


def system_root_page(request):
    context = {}
    if request.method == 'POST':
        search_qs  = request.POST['q']

        hostel_location_qs = LandlordProfile.objects.filter(hostel_location__icontains = search_qs)
        context['hostel_location_qs'] = hostel_location_qs
        # print(hostel_location_qs)
        # return redirect('/')
        return render(request, 'system_search.html', context)
    else:
        universities = LandlordProfile.objects.all()
        accommodation = HostelHomePage.objects.all()
        context['universities'] = universities
        context['accommodation'] = accommodation
        return render(request, 'system_home.html', context)


# STATIC_URL = '/static/'
# MEDIA_URL = '/media'
# STATICFILES_DIRS = [BASE_DIR+"/assets",]
# STATIC_ROOT = "/home/jersmexa/myproject/public/static"
# MEDIA_ROOT = "/home/jersmexa/myproject/public/media"

