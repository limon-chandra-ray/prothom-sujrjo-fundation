from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from psf.models import Event,ShelterChild,Slider,UserContact
from user.models import CustomUser
from staff.models import StaffProfile,Staff
from child.models import ChildProfile,Child
from sadmin.decorators import super_admin_access_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import json
# Create your views here.
@login_required()
@super_admin_access_only()
def dashboard(request):
    return render(request,'super-admin/dashboard/dashboard.html')


def change_password_view(request):
    return render(request,'super-admin/profile/change-password.html')

def super_admin_logout(request):
    logout(request)
    return redirect('sadmin:dashboard')

def edit_profile_view(request):
    return render(request,'super-admin/profile/edit-profile.html')
def edit_profile_save(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        email = request.POST['email']
        
        check_email = CustomUser.objects.filter(email = email).exclude(id = request.user.id).count()
        if check_email == 0:
            CustomUser.objects.filter(id = request.user.id).update(
                user_name = user_name,
                email = email
            )
            messages.add_message(request,messages.SUCCESS,'your profile information updated successfully')
        else:
            messages.add_message(request,messages.ERROR,'your profile not updated')
    return redirect('sadmin:edit_profile_view')
# event view section
@super_admin_access_only()
def event_list(request):
    events = Event.objects.all()
    context = {
        'events':events
    }
    return render(request,'super-admin/event/event-list.html',context)
@super_admin_access_only()
def event_add(request):
    if request.method == 'POST':
        event_title = request.POST['event_title']
        event_date = request.POST['event_date']
        event_time = request.POST['event_time']
        event_type = request.POST['event_type']
        try:
            if request.POST['event_status']:
                event_status = True
        except:
            event_status = False
        event_image = request.FILES['event_image']
        event_description = request.POST['event_description']
        event_save = Event.objects.create(
            event_title = event_title,
            event_image = event_image,
            event_date = event_date,
            event_time = event_time,
            event_type = event_type,
            event_status = event_status,
            event_description = event_description
        )
        if event_save:
            messages.add_message(request,messages.SUCCESS,'new event create successfully')
            return redirect('sadmin:event_list')

@super_admin_access_only()
def event_get(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        event = Event.objects.filter(id = int(event_id)).values('id',
                                                                     'event_title',
                                                                     'event_image',
                                                                     'event_date',
                                                                     'event_time',
                                                                     'event_status',
                                                                     'event_type',
                                                                     'event_description'
                                                                     ).first()
        return JsonResponse({'status':"Success",'event':event},safe=False)
@super_admin_access_only()
def event_edit(request):
    if request.method == 'POST':
        event_id_edit = request.POST['event_id_edit']
        event_title_edit = request.POST['event_title_edit']
        event_date_edit = request.POST['event_date_edit']
        event_time_edit = request.POST['event_time_edit']
        event_type_edit = request.POST['event_type_edit']
        try:
            if request.POST['event_status_edit']:
                event_status_edit = True
        except:
            event_status_edit = False
        try:
            event_image_edit = request.FILES['event_image_edit']
        except:
            event_image_edit = None    
        
        event_description_edit = request.POST['event_description_edit']
        event_save = Event.objects.get(id= event_id_edit)
        event_save.event_title = event_title_edit
        if event_image_edit is not None:
            event_save.event_image = event_image_edit
        event_save.event_date = event_date_edit
        event_save.event_time = event_time_edit
        event_save.event_type = event_type_edit
        event_save.event_status = event_status_edit
        event_save.event_description = event_description_edit
        event_save.save()
        messages.add_message(request,messages.SUCCESS,f'{event_title_edit} event update successfully')
        return redirect('sadmin:event_list')
    else:
        messages.add_message(request,messages.SUCCESS,'update not successfully')
        return redirect('sadmin:event_list')
@super_admin_access_only()
def event_delete(request,event_id):
    event = Event.objects.filter(id = event_id).first()
    if event:
        event.delete()
        messages.add_message(request,messages.WARNING,f'{event.event_title} event not delete')
        return redirect('sadmin:event_list')
    else:
        messages.add_message(request,messages.WARNING,f'{event.event_title} event not delete')
        return redirect('sadmin:event_list')
# children view section
@super_admin_access_only()
def children_list(request):
    childrens = ChildProfile.objects.all()
    context = {
        'childrens':childrens
    }
    return render(request,'super-admin/children/children-list.html',context)
@super_admin_access_only()
def children_create_view(request):
    blood_group = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
    context = {
        'blood_group':blood_group
    }
    return render(request,'super-admin/children/add-children.html',context)
@super_admin_access_only()
def children_save(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        phone_number = request.POST['phone_number']
        date_of_birth = request.POST['date_of_birth']
        birth_certificate = request.POST['birth_certificate']
        child_height = request.POST['child_height']
        child_weight = request.POST['child_weight']
        child_blood = request.POST['child_blood']
        child_image = request.FILES['child_image']
        pre_address = request.POST['pre_address']
        par_address = request.POST['par_address']
        description = request.POST['description']
        check_birth_certificate = ChildProfile.objects.filter(
            child_birth_certificate_number = birth_certificate
        ).count()
        check_phone_number = ChildProfile.objects.filter(
            child_phone_number = phone_number
        ).count()
        if check_birth_certificate < 1 and check_phone_number < 1:
            last_child = CustomUser.objects.last()
            email_address = f"{user_name}{last_child.id}@gmail.com"
            custom_user= Child.objects.create_child(
                user_name = user_name,
                email = email_address,
                password = phone_number
            )
            custom_user.save()
            child_profile = ChildProfile.objects.filter(child_user=custom_user).first()
            child_profile.child_first_name = first_name
            child_profile.child_last_name = last_name
            child_profile.child_phone_number = phone_number
            child_profile.child_image = child_image
            child_profile.child_father_name = father_name
            child_profile.child_mother_name = mother_name
            child_profile.child_date_of_birth = date_of_birth
            child_profile.child_birth_certificate_number = birth_certificate
            child_profile.child_blood = child_blood
            child_profile.child_weight = child_weight
            child_profile.child_height = child_height
            child_profile.child_present_address = pre_address
            child_profile.child_parmanent_address = par_address
            child_profile.child_description = description
            child_profile.save()
            messages.add_message(request,messages.SUCCESS,'new children added successfully')
            return redirect('sadmin:children_list')
        else:
            messages.add_message(request,messages.WARNING,'birth certificate number all-ready added')
    return redirect('sadmin:children_create_view')
@super_admin_access_only()
def children_info_update_view(request,children_id):
    update_child = ChildProfile.objects.get(id = children_id)
    blood_group = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
    context = {
        'child': update_child,
        'blood_group':blood_group
    }
    return render(request,'super-admin/children/edit-children.html',context)
@super_admin_access_only()
def children_info_update_save(request,children_id):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        user_name = request.POST['user_name']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        date_of_birth = request.POST['date_of_birth']
        birth_certificate = request.POST['birth_certificate']
        child_height = request.POST['child_height']
        child_weight = request.POST['child_weight']
        child_blood = request.POST['child_blood']
        try:
            child_image = request.FILES['child_image']
        except:
            child_image = None
        pre_address = request.POST['pre_address']
        par_address = request.POST['par_address']
        description = request.POST['description']
        
        birth_certificate_check = ChildProfile.objects.exclude(id=children_id).filter(child_birth_certificate_number = birth_certificate).count()
        if birth_certificate_check < 1:
            child_profile = ChildProfile.objects.get(id= children_id)
            child_profile.child_first_name = first_name
            child_profile.child_last_name = last_name
            child_profile.child_phone_number = phone_number
            if child_image is not None:
                child_profile.child_image = child_image
            child_profile.child_father_name = father_name
            child_profile.child_mother_name = mother_name
            child_profile.child_date_of_birth = date_of_birth
            child_profile.child_birth_certificate_number = birth_certificate
            child_profile.child_blood = child_blood
            child_profile.child_weight = child_height
            child_profile.child_height = child_weight
            child_profile.child_present_address = pre_address
            child_profile.child_parmanent_address = par_address
            child_profile.child_description = description 
            child_profile.save()
            user = CustomUser.objects.get(id = child_profile.child_user.id)
            user.user_name = user_name
            user.save()
            messages.add_message(request,messages.SUCCESS,'new children added successfully')
            return redirect('sadmin:children_list')
        else:
            messages.add_message(request,messages.SUCCESS,'Please add unique birth cirtificate number')
    return redirect('sadmin:children_info_update_view',children_id)
@super_admin_access_only()    
def children_info_delete(request,children_id):
    child_data = CustomUser.objects.filter(id = children_id).first()
    if child_data:
        child_data.delete()
        messages.add_message(request,messages.SUCCESS,f'{child_data.user_name} information delete successfully')
        return redirect('sadmin:children_list')
    
def children_detail_view(request,children_id):
    pass


def office_staff_list(request):
    staffs = CustomUser.objects.filter(role = 'STAFF',is_active = True).order_by('-id')
    context = {
        'staffs':staffs
    }
    return render(request,'super-admin/staff/staff-list.html',context)

def office_staff_add_view(request):
    
    return render(request,'super-admin/staff/staff-add.html')

def office_staff_add(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        user_name = request.POST['user_name']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email_address']
        staff_image = request.FILES['staff_image']
        email_check = CustomUser.objects.filter(email = email_address).count()
        if email_check < 1:
            office_save = Staff.objects.create_office_staff(
                user_name = user_name,
                email = email_address,
                password = phone_number
            )
            office_save.save()
            staff_profile = StaffProfile.objects.filter(staff_user = office_save).first()
            staff_profile.staff_full_name = f_name
            staff_profile.staff_image = staff_image
            staff_profile.save()
            messages.add_message(request,messages.SUCCESS,'New office member add successfully')
            return redirect('sadmin:office_staff_list')
        else:
            messages.add_message(request,messages.WARNING,'Email address added all-ready')
            return redirect('sadmin:office_staff_add_view')
def office_staff_edit(request):
    if request.method == 'POST':
        user  =request.POST['user_id']
        f_name  =request.POST['f_name']
        user_name  =request.POST['user_name']
        phone_number  =request.POST['phone_number']
        email  =request.POST['email_address']
        try:
            
            staff_image  = request.FILES['staff_image']
        except:
            staff_image = None
        CustomUser.objects.filter(id = int(user)).update(
            user_name = user_name,
            email = email
        )
        custom_user = CustomUser.objects.get(id = int(user))
        profile = StaffProfile.objects.filter(staff_user = custom_user).first()
        profile.staff_full_name = f_name
        profile.staff_phone_number = phone_number
        if staff_image is not None:
            profile.staff_image = staff_image
        profile.save()
        messages.add_message(request,messages.SUCCESS,'Staff profile update successfully')
        return redirect('sadmin:office_staff_list')
    
def staff_get(request):
    if request.method == 'POST':
        staff_id = request.POST['staff']
        user = CustomUser.objects.filter(id = int(staff_id)).values('id','user_name','email').first()
        profile = StaffProfile.objects.filter(staff_user__id= int(staff_id)).values('staff_full_name','staff_phone_number','staff_image').first()
        
        return JsonResponse({'status':"success","userstaff":user,'staffProfile':profile},safe=False) 

def staff_delete(request,staff_id):
    user_active_status_change = CustomUser.objects.filter(id = staff_id).update(
        is_active = False
    )
    if user_active_status_change:
        messages.add_message(request,messages.SUCCESS,'Staff Account deleted')
        return redirect('sadmin:office_staff_list')
    

def slider_image_list(request):
    sliders = Slider.objects.all().order_by('-slider_status')
    context = {
        'sliders' : sliders
    }
    return render(request,'super-admin/slider/slider-list.html',context)
def slider_image_add(request):
    if request.method == 'POST':
        slide_title = request.POST['slide_title']
        slide_description = request.POST['slider_description']
        slide_image = request.FILES['slide_image']
        slider = Slider.objects.create(
            slider_caption = slide_title,
            slider_image = slide_image,
            slider_description = slide_description
        )
        if slider:
            messages.add_message(request,messages.SUCCESS,'new slide created successfully')
            return redirect('sadmin:slider_image_list')

def get_slide(request):
    if request.method == 'POST':
        slide_id = request.POST['slide']
        slide = Slider.objects.filter(id = int(slide_id)).values('id','slider_caption','slider_image','slider_description').first()
        return JsonResponse({"status":"success",'slide':slide},safe=True)
def slider_image_edit(request):
    if request.method == 'POST':
        slide_id = request.POST['slide']
        slide_title = request.POST['slide_title']
        slide_description = request.POST['slider_description']
        try:
            slide_image = request.FILES['eidt_slide_image']
        except:
            slide_image = None
        slider = Slider.objects.get(id = int(slide_id))
        slider.slider_caption = slide_title
        slider.slider_description = slide_description
        if slide_image is not None:
             slider.slider_image = slide_image
        if slider:
            slider.save()
            messages.add_message(request,messages.SUCCESS,' slide image update successfully')
            return redirect('sadmin:slider_image_list')


def slider_image_status_change(request,image_id):
    slide = Slider.objects.get(id = image_id)

    if slide.slider_status == True:
        slide.slider_status = False
    else:
        slide.slider_status = True
    
    slide.save()
    messages.add_message(request,messages.SUCCESS,'slider status change successfully')
    return redirect("sadmin:slider_image_list")


# video view section
def video_list(request):
    # sliders = Slider.objects.all().order_by('slider_status')
    # context = {
    #     'sliders' : sliders
    # }
    return render(request,'super-admin/video/video-list.html')



def child_sponsor_list_view(request):
    sponsors = CustomUser.objects.filter(role = "SPONSOR").order_by('is_active')
    context = {
        'sponsors':sponsors
    }
    return render(request,'super-admin/child-sponsor/child-sponsor-list.html',context)

def sponsor_detail_view(request):
    return render(request,'super-admin/child-sponsor/child-sponsor-detail.html')

# authentication system view section
def login_view(request):
    return render(request,'super-admin/auth/log-in.html')


# contact us section
def contact_information_save(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        title = request.POST['title']
        message = request.POST['message']

        user_contact = UserContact.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            title = title,
            contact_message = message
        )
        user_contact.save()
        messages.add_message(request,messages.SUCCESS,'your contact information submit successfully')
    else:
        messages.add_message(request,messages.WARNING,'your contact information not submited')
    return redirect("psf:contact_us")

def contact_information_list(request):
    user_contacts = UserContact.objects.all().order_by("uc_status")
    context ={
        'user_contacts': user_contacts
    }
    return render(request,'super-admin/contact/contact-list.html',context)