
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from psf.views import error_404_view,error_500_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('psf.urls',namespace='psf')),
    path('super-admin/',include('sadmin.urls',namespace='sadmin')),
    path('office-staff/',include('staff.urls',namespace='staff')),
    path('management-sponsor/',include('sponsor.urls',namespace='sponsor')),
    path('user-authentication/',include('auth_user.urls',namespace='auth_user'))
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

handler404 = error_404_view
handler500 = error_500_view