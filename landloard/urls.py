from django.urls import path
from . import views as user_views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', user_views.register, name = 'register'),
    path('login/', user_views.login_landlord, name = 'login_landlord'),
    path('dashboard/', user_views.dashboard_landlord, name='dashboard_landlord'),
    path('profile/', user_views.dashboard_landlord_profile, name = 'profile'),
    path('hostelprofile/', user_views.dashboard_landlord_hostel_profile, name = 'dashboard_landlord_hostel_profile'),
    # path('stripe_payments/', user_views.stripe_payments, name='stripe_payments'),
    # path('payments/', user_views.payments, name = 'payments'),
    path('logout/', user_views.loguot_landlord, name='loguot_landlord'),
    path('stuff/', user_views.inform_Admin_Make_landlord_staff, name='inform_Admin_Make_landlord_staff')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)