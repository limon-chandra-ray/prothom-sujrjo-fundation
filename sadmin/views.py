from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from psf.models import Event,ShelterChild,Slider
from user.models import CustomUser
from staff.models import StaffProfile,Staff
import json
# Create your views here.
def dashboard(request):
    return render(request,'super-admin/dashboard/dashboard.html')


# event view section
def event_list(request):
    events = Event.objects.all()
    context = {
        'events':events
    }
    return render(request,'super-admin/event/event-list.html',context)
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
def children_list(request):
    childrens = ShelterChild.objects.all()
    context = {
        'childrens':childrens
    }
    return render(request,'super-admin/children/children-list.html',context)

def children_create_view(request):
    blood_group = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
    context = {
        'blood_group':blood_group
    }
    return render(request,'super-admin/children/add-children.html',context)
def children_save(request):
    if request.method == 'POST':
        try:
            f_name = request.POST['f_name']
            user_name = request.POST['user_name']
            father_name = request.POST['father_name']
            mother_name = request.POST['mother_name']
            date_of_birth = request.POST['date_of_birth']
            birth_certificate = request.POST['birth_certificate']
            child_height = request.POST['child_height']
            child_weight = request.POST['child_weight']
            child_blood = request.POST['child_blood']
            child_image = request.FILES['child_image']
            pre_address = request.POST['pre_address']
            par_address = request.POST['par_address']
            description = request.POST['description']
            check_birth_certificate = ShelterChild.objects.filter(
                child_birth_certificate_number = birth_certificate
            ).first()
            if check_birth_certificate is None:
                shelter_child = ShelterChild.objects.create(
                    child_name = user_name,
                    child_full_name = f_name,
                    child_image = child_image,
                    child_father_name = father_name,
                    child_mother_name = mother_name,
                    child_date_of_birth = date_of_birth,
                    child_birth_certificate_number = birth_certificate,
                    child_blood = child_blood,
                    child_weight = child_height,
                    child_height = child_weight,
                    child_present_address = pre_address,
                    child_parmanent_address = par_address,
                    child_description = description 
                )
                if shelter_child:
                    shelter_child.save()
                    messages.add_message(request,messages.SUCCESS,'new children added successfully')
                    return redirect('sadmin:children_list')
            else:
                messages.add_message(request,messages.WARNING,'birth certificate number all-ready added')
            
        except:
            messages.add_message(request,messages.ERROR,'please fill-up all fields')
    return redirect('sadmin:children_create_view')
def children_info_update_view(request,children_id):
    update_child = ShelterChild.objects.get(id = children_id)
    blood_group = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
    context = {
        'child': update_child,
        'blood_group':blood_group
    }
    return render(request,'super-admin/children/edit-children.html',context)

def children_info_update_save(request,children_id):
    if request.method == 'POST':
        
        f_name = request.POST['f_name']
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
        
        shelter_child = ShelterChild.objects.get(id= children_id)
        shelter_child.child_name = user_name
        shelter_child.child_full_name = f_name
        if child_image is not None:
            shelter_child.child_image = child_image
        shelter_child.child_father_name = father_name
        shelter_child.child_mother_name = mother_name
        shelter_child.child_date_of_birth = date_of_birth
        shelter_child.child_birth_certificate_number = birth_certificate
        shelter_child.child_blood = child_blood
        shelter_child.child_weight = child_height
        shelter_child.child_height = child_weight
        shelter_child.child_present_address = pre_address
        shelter_child.child_parmanent_address = par_address
        shelter_child.child_description = description 
        shelter_child.save()
        
        messages.add_message(request,messages.SUCCESS,'new children added successfully')
        return redirect('sadmin:children_list')
           
    return redirect('sadmin:children_info_update_view',children_id)
    
def children_info_delete(request,children_id):
    child_data = ShelterChild.objects.filter(id = children_id).first()
    if child_data:
        child_data.delete()
        messages.add_message(request,messages.SUCCESS,f'{child_data.child_name} information delete successfully')
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
    sliders = Slider.objects.all().order_by('slider_status')
    context = {
        'sliders' : sliders
    }
    return render(request,'super-admin/slider/slider-list.html',context)
def slider_image_add(request):
    pass
def slider_image_edit(request,image_id):
    pass

def slider_image_status_change(request,image_id):
    pass


# video view section
def video_list(request):
    # sliders = Slider.objects.all().order_by('slider_status')
    # context = {
    #     'sliders' : sliders
    # }
    return render(request,'super-admin/video/video-list.html')