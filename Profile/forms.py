from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import LandlordProfile, TenantProfile, UserHostelPlan, HostelPaymentplan
from landloard.models import HostelPlan


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'id_email', 'required': 'true'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'id_username', 'required': 'true'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TenantProfileForm(forms.ModelForm):
    """Form definition for TenantProfile."""
    your_full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))

    class Meta:
        """Meta definition for TenantProfileform."""

        model = TenantProfile
        fields = [
            # 'user',
            'your_full_name',
            'phone_number',
            'user_picture',
        ]

# TEST_CHOICES = [[x.mpesa_shotcode, f'{x.hostel_name,x.mpesa_shotcode}'] for x in HostelPlan.objects.all()]


class PaymentForm(forms.Form):
    # test = forms.MultipleChoiceField(choices=TEST_CHOICES, required=False)
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'id_number', 'required': 'true'}))
    user_id = forms.CharField(widget=forms.TextInput(
        attrs={'hidden': 'true', 'value': '{{ user.id }}', 'id': 'id_number', 'required': 'true'}))


class UserHostelPlanForm(forms.ModelForm):
    """Form definition for UserHostelPlanForm."""

    class Meta:
        """Meta definition for UserHostelPlanForm."""

        model = UserHostelPlan
        fields = [
            # 'tenant',
            'plan',
        ]


class HostelPaymentplanForm(forms.ModelForm):
    """Form definition for HostelPaymentplan."""

    class Meta:
        """Meta definition for HostelPaymentplanform."""

        model = HostelPaymentplan
        fields = [
            # 'tenant',
            # 'paymentplan',
            # 'amountpaid',
        ]


class LandlordLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'id_username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'validate', 'id': 'id_password', 'required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(LandlordLoginForm, self).clean(*args, **kwargs)


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'id': 'id_username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'validate', 'id': 'id_password', 'required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(UserLoginForm, self).clean(*args, **kwargs)
