
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('psf.urls',namespace='psf')),
    path('super-admin/',include('sadmin.urls',namespace='sadmin')),
    path('office-staff/',include('staff.urls',namespace='staff')),
    path('sponsor/',include('sponsor.urls',namespace='sponsor')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)