from django.shortcuts import render,redirect
from user.models import CustomUser
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def login_view(request):
    return render(request,'user/login.html')

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
      
     
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        con_password = request.POST['con_password']
        pass_len = len(new_password) >= 6
        pass_same = new_password == con_password
        if pass_len and pass_same:
            check_user = CustomUser.objects.get(id = request.user.id)
            check_pass = request.user.check_password(old_password)
            if check_user and check_pass:
                CustomUser.objects.filter(id = request.user.id).update(
                    password = make_password(new_password)
                )
                logout(request)
                messages.add_message(request,messages.SUCCESS,'your password change Please login again')
                return redirect("sadmin:dashboard")
            else:
                messages.add_message(request,messages.WARNING,'your old password not match')
        else:
            messages.add_message(request,messages.WARNING,'password min length 6 or password not match')
    return redirect('sadmin:change_password_view')