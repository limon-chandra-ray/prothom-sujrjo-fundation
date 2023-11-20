from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def user_authenticated_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            if request.user.role == "ADMIN":
                print('role not satisfy student')
                messages.add_message(request,messages.SUCCESS,'Successfully connect')
                return redirect("sadmin:dashboard")
            # elif request.user.role == "TEACHER":
            #     print('role not satisfy teacher')
            #     messages.add_message(request,messages.SUCCESS,'Successfully connect')
            #     return redirect("teacher:home")
            # elif request.user.role == "STAFF":
            #     print('role not satisfy staff')
            #     messages.add_message(request,messages.SUCCESS,'Successfully connect')
            #     return redirect("staff:home")
            else:
                logout(request)
                messages.add_message(request,messages.WARNING,'Your are not authenticated user')
                return redirect('psf:login_view')
        else:
            messages.add_message(request,messages.ERROR,'Your are not authenticated user')
            context={
                'email':email
            }
            return redirect('psf:login_view')