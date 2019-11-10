from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from . forms import RoomateSelectionForm, UserRegisterForm, UserLoginForm, PaymentForm, TenantProfileForm, UserHostelPlanForm, HostelPaymentplanForm
from . import lipanampesa
from urllib3.exceptions import ProtocolError, ConnectionError
# m-pesa
import requests
import json
from .access_token import generate_access_token
from .utils import timestamp_convertion
from . import keys
from requests.auth import HTTPBasicAuth
from .encode_base64 import generate_password
#
from . models import PaymentRequestHeaders, TenantProfile, UserHostelPlan, HostelPaymentplan, RoomateSelection
from mpesa.models import LNMOnline
from landloard.models import HostelPlan


#
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('/user/')  # will change to dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'student_profile/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        messages.success(
            request, f'login was Success!{ request.user.username}')
        return redirect('/user/dashboard/')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, f'login was Success {username} !!!')
            return redirect('/user/dashboard/')
        else:
            messages.success(
                request, f'login Error !!!! Provide Correct Username And Password')
    else:
        form = UserLoginForm()
    return render(request, 'student_profile/login.html', {'form': form})


@login_required(login_url='/user/')
def user_dashboard(request):
    context = {}
    # if request.user.is_authenticated:

    return render(request, 'student_profile/studentpages/dashboard.html', context)


@login_required(login_url='/user/')
def profile(request):
    context = {}
    if request.user.is_authenticated:
        user_qs = TenantProfile.objects.filter(user_id=request.user.id)
        context = {}
        if request.method == 'POST':
            form = TenantProfileForm(request.POST, request.FILES)
            context['form'] = form
            if form.is_valid():
                your_full_name = form.cleaned_data.get('your_full_name')

                user_qs = TenantProfile.objects.filter(user_id=request.user.id)
                context['user_qs'] = user_qs
                if user_qs.count() == 1:
                    user = user_qs.first()
                    if user:
                        messages.success(
                            request, f'You Already Have A Profile {your_full_name} !')
                        return redirect('/user/profile/')
                else:
                    messages.success(
                        request, f'Account Profile for {your_full_name} is Created !')
                    obj = form.save(commit=False)
                    obj.user_id = request.user.id
                    obj.save()
                    return redirect('/user/profile/')
            else:
                messages.success(request, f'Fill All Required fields !!')
        else:
            form = TenantProfileForm()
            context['form'] = form
            context['user_qs'] = user_qs

    return render(request, 'student_profile/studentpages/profile.html', context)


@login_required(login_url='/user/')
def all_user_transaction(request):
    context = {}
    if request.user.is_authenticated:
        previous_transaction = PaymentRequestHeaders.objects.filter(
            user=request.user.id)
        lnmponline = LNMOnline.objects.all()
        context['lnmponline'] = lnmponline
        context['previous_transaction'] = previous_transaction

    return render(request, 'student_profile/studentpages/transaction.html', context)


@login_required(login_url='/user')
def user_roomate_selection(request):
    context = {}
    if request.user.is_authenticated:
        hostel_payment_plan = HostelPaymentplan.objects.all()
        hostel_payment_plan_qs = HostelPaymentplan.objects.filter(tenant_id = request.user.id).first()
        user_hostel_plan = UserHostelPlan.objects.filter(tenant_id = request.user.id)
        roomate_qs = RoomateSelection.objects.filter(user_id = request.user.id)
        context['hostel_payment_plan'] = hostel_payment_plan
        context['hostel_payment_plan_qs'] = hostel_payment_plan_qs
        context['user_hostel_plan'] = user_hostel_plan
        context['roomate_qs'] = roomate_qs
        if request.method == 'POST':
            roomate_selecton_save = RoomateSelection.objects.create(
                user_id = request.POST['user_id'],
                user_roomate = request.POST['user_roomate'],
                is_accepted = request.POST['is_accepted'],
            )
            roomate_selecton_save.save()
            return redirect('/user/roomate/')
        else:
            form = RoomateSelectionForm()
            context['form'] = form
        return render(request, 'student_profile/studentpages/roomate.html', context)


@login_required(login_url='/user/')
def payments(request):
    context = {}

    if request.user.is_authenticated:
        hostelplan = HostelPlan.objects.all()
        previous_transaction = PaymentRequestHeaders.objects.filter(
            user=request.user.id)
        hostel_plan_check_qs = UserHostelPlan.objects.filter(
            tenant=request.user.id)  # tenant->user request.user.landlordprofile.id
        hostel_payment_plan_check_qs = HostelPaymentplan.objects.filter(
            tenant=request.user.id)
        # hostel_plan_check_qs = UserHostelPlan.objects.all()
        context['hostel_plan_check_qs'] = hostel_plan_check_qs
        context['previous_transaction'] = previous_transaction
        context['hostelplan'] = hostelplan
        context['hostel_payment_plan_check_qs'] = hostel_payment_plan_check_qs
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        plan_form = UserHostelPlanForm(request.POST)
        hostel_payment_plan_form = HostelPaymentplanForm(request.POST)
        context['form'] = form
        context['plan_form'] = plan_form
        context['hostel_payment_plan_form'] = hostel_payment_plan_form
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            user_id = form.cleaned_data.get('user_id')
            # time formatting
            formarted_time = timestamp_convertion()
            # to be implemented on production scale
            business_short_code = request.POST['business_short_code']

            hostel_name = request.POST['hostel_name_id']
            amount_payable = request.POST['amount']

            # base64 encode
            decoded_password = generate_password(formarted_time)
            access_token = generate_access_token()
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": keys.business_short_code,
                "Password": decoded_password,
                "Timestamp": formarted_time,
                "TransactionType": "CustomerBuyGoodsOnline",  # CustomerPayBillOnline
                "Amount": amount_payable,
                "PartyA": phone_number,
                "PartyB": keys.business_short_code,
                "PhoneNumber": phone_number,
                "CallBackURL": "https://accomodations.herokuapp.com/api/payments/lnm/",
                "AccountReference": "Test004Clinton",
                "TransactionDesc": "Rent pay"
            }

            response = requests.post(api_url, json=request, headers=headers)

            mystr = response.text
            obbstr = json.loads(mystr)
            merchant_request_id = obbstr['MerchantRequestID']
            checkout_request_id = obbstr['CheckoutRequestID']
            response_description = obbstr['ResponseDescription']

            payment_request_headers = PaymentRequestHeaders.objects.create(
                merchant_request_id=merchant_request_id,
                checkout_request_id=checkout_request_id,
                response_description=response_description,
                user_id=user_id,
                hostel_name_id=hostel_name,
                phone_number_used_for_payment=phone_number,
            )

            context['checkout_request_id'] = checkout_request_id
            context['response_description'] = response_description
            payment_request_headers.save()

            return redirect('/user/payments/')
        elif plan_form.is_valid():
            messages.success(
                request, f"{plan_form.cleaned_data.get('plan')} Selected Successfully")
            obj = plan_form.save(commit=False)
            obj.tenant_id = request.user.id
            obj.save()
            return redirect('/user/payments/')
        elif hostel_payment_plan_form.is_valid():
            messages.success(
                request, f"{request.POST['amountpaid']} Selected Successfully")
            obj = hostel_payment_plan_form.save(commit=False)
            obj.tenant_id = request.user.id
            obj.paymentplan_id = hostel_name = request.POST['paymentplan_id']
            obj.amountpaid = hostel_name = request.POST['amountpaid']
            obj.save()
    else:
        hostel_payment_plan_form = HostelPaymentplanForm()
        plan_form = UserHostelPlanForm()
        form = PaymentForm()
        context['hostel_payment_plan_form'] = hostel_payment_plan_form
        context['form'] = form
        context['plan_form'] = plan_form
    return render(request, 'student_profile/studentpages/pay.html', context)


def user_loguot(request):
    logout(request)
    messages.success(request, f'You Have logout !!!')
    return redirect('/user/')


@login_required
def stripe_payments(request):
    context = {}

    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            return redirect('/Accounts/payments/')

    else:
        form = PaymentForm()
        context['form'] = form
    return render(request, 'student_profile/payments/pay.html', context)
