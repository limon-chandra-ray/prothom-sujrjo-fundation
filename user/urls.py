from django.urls import path
app_name ='user'
from . import views
urlpatterns = [
 path('user-authenticate-check',views.user_authenticated_check,name='user_authenticated_check')   
]
