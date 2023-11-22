from django.urls import path
app_name = 'auth_user'
from . import views
urlpatterns = [
    path('user-authenticate-check',views.user_authenticated_check,name='user_authenticated_check'),
    path('change-password',views.change_password,name='change_password')
]
