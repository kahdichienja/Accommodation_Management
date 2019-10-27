from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from Profile.forms import UserRegisterForm, LandlordLoginForm
from .models import LandlordProfile, HostelHomePage, HostelService, HostelContact,HostelGallary, HostelPlan
from .forms import LandlordProfileForm, HostelHompageForm, HostelPlanForm, HostelServiceForm, HostelContactForm, HostelGallaryForm
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('/management/login/') 
    else:
        form = UserRegisterForm()    
    return render(request, 'pages/register.html', {'form': form})


def login_landlord(request):
    if request.user.is_authenticated:
        messages.success(request, f'login was Success!{ request.user.username}')
        return redirect('/management/dashboard/')
    if request.method == 'POST':
        form = LandlordLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, f'login was Success {username} !!!')
            return redirect('/management/dashboard/')

        else:
            messages.success(request, f'login Error !!!! Provide Correct Username And Password')
    else:
        form = LandlordLoginForm()    
    return render(request, 'pages/login.html', {'form': form})


@login_required(login_url='/management/login/')
@staff_member_required(login_url='/management/stuff/')
def dashboard_landlord(request):
    if request.user.is_authenticated:
        try:
            hostel_plan = HostelPlan.objects.filter(hostel_name_id = request.user.landlordprofile.id)
        except ObjectDoesNotExist:
            messages.success(request, f'{request.user.username} Create Your Profile First !')
            return redirect('/management/profile/')
        return render(request, 'pages/dashboard.html', {
            'hostel_plan':hostel_plan,
        })

@login_required(login_url='/management/login/')
@staff_member_required(login_url='/management/stuff/')
def dashboard_landlord_hostel_profile(request):
    if request.user.is_authenticated:
        # hostel_home_page_qs = HostelHomePage.objects.filter(hostel_name_id = request.user.landlordprofile.id)
        try:
            hostel_home_page_qs = HostelHomePage.objects.filter(hostel_name_id = request.user.landlordprofile.id)
        except ObjectDoesNotExist:
            messages.success(request, f'{request.user.username} Create Your Profile First !')
            return redirect('/management/profile/')
        hostel_contact_qs = HostelContact.objects.filter(hostel_name_id = request.user.landlordprofile.id)
        hostel_service_qs = HostelService.objects.filter(hostel_name_id = request.user.landlordprofile.id)
        hostel_gallery_qs = HostelGallary.objects.filter(hostel_name_id = request.user.landlordprofile.id)
        if request.method == 'POST':
            hostelhompageform = HostelHompageForm(request.POST, request.FILES)
            hostelplanform = HostelPlanForm(request.POST)
            hostelserviceform = HostelServiceForm(request.POST)
            hostelcontact = HostelContactForm(request.POST)
            hostelgalleryform = HostelGallaryForm(request.POST, request.FILES)
            if hostelhompageform.is_valid():
                obj = hostelhompageform.save(commit = False)
                obj.hostel_name_id = request.user.landlordprofile.id
                obj.save()
                messages.success(request, f'{request.user.landlordprofile.hostel_name} Home Page Created Successfully !')
                return redirect('/management/hostelprofile/') 
            
            elif hostelplanform.is_valid():
                obj = hostelplanform.save(commit = False)
                obj.hostel_name_id = request.user.landlordprofile.id
                obj.save()
                messages.success(request, f'{request.user.landlordprofile.hostel_name} Plan Created Successfully !')
                return redirect('/management/hostelprofile/') 

            elif hostelserviceform.is_valid():
                obj = hostelserviceform.save(commit = False)
                obj.hostel_name_id = request.user.landlordprofile.id
                obj.save()
                messages.success(request, f'{request.user.landlordprofile.hostel_name} Services Created Successfully !')
                return redirect('/management/hostelprofile/') 

            elif hostelcontact.is_valid():
                obj = hostelcontact.save(commit = False)
                obj.hostel_name_id = request.user.landlordprofile.id
                obj.save()
                messages.success(request, f'{request.user.landlordprofile.hostel_name} Contact Created Successfully !')
                return redirect('/management/hostelprofile/') 
            elif hostelgalleryform.is_valid():
                obj = hostelgalleryform.save(commit = False)
                obj.hostel_name_id = request.user.landlordprofile.id
                obj.save()
                messages.success(request, f'{request.user.landlordprofile.hostel_name} Gallery Created Successfully !')
                return redirect('/management/hostelprofile/') 
                
        else:
            hostelhompageform = HostelHompageForm()
            hostelplanform = HostelPlanForm()
            hostelserviceform = HostelServiceForm()
            hostelcontact = HostelContactForm()
            hostelgalleryform = HostelGallaryForm()

        return render(request, 'pages/hostel_profile.html', {
            'hostelhompageform':hostelhompageform,
            'hostelplanform': hostelplanform,
            'hostelserviceform': hostelserviceform,
            'hostelcontact': hostelcontact,
            'hostelgalleryform': hostelgalleryform,
            'hostel_home_page_qs': hostel_home_page_qs,
            'hostel_service_qs': hostel_service_qs,
            'hostel_contact_qs': hostel_contact_qs,
            'hostel_gallery_qs': hostel_gallery_qs,
        })

@login_required(login_url='/management/login/')
@staff_member_required(login_url='/management/stuff/')
def dashboard_landlord_profile(request):
    if request.user.is_authenticated:
        user_qs = LandlordProfile.objects.filter(user_id = request.user.id)
        context = {}
        if request.method == 'POST':
            form = LandlordProfileForm(request.POST, request.FILES)
            context['form'] = form
            if form.is_valid():
                your_full_name = form.cleaned_data.get('your_full_name')

                user_qs = LandlordProfile.objects.filter(user_id = request.user.id)
                context['user_qs'] = user_qs
                if user_qs.count() == 1:
                    user = user_qs.first()
                    if user:
                        messages.success(request, f'You Already Have A Profile {your_full_name} !')
                        return redirect('/management/profile/')
                else:
                    messages.success(request, f'Account Profile for {your_full_name} is Created !')
                    obj = form.save(commit = False)
                    obj.user_id = request.user.id
                    obj.save()
                    return redirect('/management/profile/')
        else:
            form = LandlordProfileForm() 
            context['form'] = form
            context['user_qs'] = user_qs       
        return render(request, 'pages/my_profile.html', context)




def loguot_landlord(request): 
    logout(request)  
    messages.success(request, f'You Have logout !!!')
    return redirect('/management/login/')
    
def inform_Admin_Make_landlord_staff(request):
    if request.user.is_authenticated:
        messages.success(request, f'login was Success!{ request.user.username}')
        messages.success(request, f'Only Staff Are Required To View The Page Your Requested. Contact Admin To Make You Staff 0797324006 !!!')
        return render(request, 'pages/stufflogin.html', {})
        # return redirect('/almasico/activities/')  
    return render(request, 'pages/stufflogin.html', {})
