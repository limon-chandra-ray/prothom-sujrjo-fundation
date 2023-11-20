from functools import wraps
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
def super_admin_test_func(user):
    if user.role == 'ADMIN':
        return True
    return False

def super_admin_access_only(view_to_return = 'sadmin:login_view'):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request,*args, **kwargs):
            if not super_admin_test_func(request.user):
                logout(request)
                messages.add_message(request,messages.WARNING,'Try again')
                return  redirect(view_to_return)
            return view(request,*args, **kwargs)
        return _wrapped_view
    return decorator