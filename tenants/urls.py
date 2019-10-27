from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('list/', views.home_hostels, name="hostels"),
    path('list/<int:pk>/', views.hostel_detailed_view, name="hostels_detailes"),
    path('gallery/<int:pk>/', views.hostel_detailed_view_gallery, name="gallery"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)