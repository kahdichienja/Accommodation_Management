from django.urls import path
from . import views as user_views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', user_views.user_login, name = 'login'),
    path('register/', user_views.register, name = 'register'),
    path('dashboard/', user_views.user_dashboard, name = 'dashboard'),
    path('logout/', user_views.user_loguot),
    path('profile/', user_views.profile, name = 'profile'),
    # path('stripe_payments/', user_views.stripe_payments, name='stripe_payments'),
    path('payments/', user_views.payments, name = 'payments'),
    path('roomate/', user_views.user_roomate_selection, name='user_roomate_selection'),
    path('alltransaction/', user_views.all_user_transaction, name='all_user_transaction'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)