from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from psf.models import (VideoGallery,Event,ShelterChild,Slider,UserContact,GalleryImage,Rank)
from user.models import CustomUser
from staff.models import StaffProfile,Staff,StaffRank
from child.models import ChildProfile,Child,ChildProgress
from sponsor.models import SponsorCall,Donate
from sadmin.decorators import super_admin_access_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import json
from PIL import Image
from datetime import date,datetime,timedelta
from django.core.files.storage import FileSystemStorage
from . import utlis
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
        hobbie = request.POST['hobbie']
        study_now = request.POST['study_now']
        admission_date = request.POST['admission_date']
        child_image = request.FILES['child_image']
        child_cover_image = request.FILES['child_cover_image']
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
            child_profile.child_cover_image = child_cover_image
            child_profile.child_hobbie = hobbie
            child_profile.child_join = admission_date
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
            child_profile.child_study = study_now
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
        hobbie = request.POST['hobbie']
        admission_date = request.POST['admission_date']
        study_now = request.POST['study_now']
        try:
            child_image = request.FILES['child_image']
        except:
            child_image = None
        try:
            child_cover_image = request.FILES['child_cover_image']
        except:
            child_cover_image = None
        pre_address = request.POST['pre_address']
        par_address = request.POST['par_address']
        description = request.POST['description']
        
        birth_certificate_check = ChildProfile.objects.exclude(id=children_id).filter(child_birth_certificate_number = birth_certificate).count()
        if birth_certificate_check < 1:
            child_profile = ChildProfile.objects.get(id= children_id)
            child_profile.child_first_name = first_name
            child_profile.child_last_name = last_name
            child_profile.child_phone_number = phone_number
            child_profile.child_hobbie = hobbie
            child_profile.child_join = admission_date
            if child_image is not None:
                child_profile.child_image = child_image
            if child_cover_image is not None:
                child_profile.child_cover_image = child_cover_image
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
            child_profile.child_study = study_now
            child_profile.save()
            CustomUser.objects.filter(id = child_profile.child_user.id).update(
                user_name = user_name
            )
            # print(user)
            # user.user_name = user_name
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

# children progress section
def child_progress_list(request,child_id):
    child = CustomUser.objects.get(id=int(child_id))
    child_progress = ChildProgress.objects.filter(child_user = child)
    context={
        'child_id':child_id,
        'child_progress':child_progress
    }
    return render(request,'super-admin/children/progress/progress-list.html',context)
def child_progress_add_view(request,child_id):
    context={
        'child_id':child_id
    }
    return render(request,'super-admin/children/progress/progress-add.html',context)
def child_progress_add_save(request,child_id):
    if request.method == 'POST':
        title = request.POST['progress_title']
        progress_year  = request.POST['progress_year']
        description  = request.POST['description']
        progress_image = request.FILES['progress_image']
        child = CustomUser.objects.get(id=int(child_id))
        child_progress = ChildProgress.objects.create(
            child_user = child,
            progress_year = progress_year,
            progress_title = title,
            progress_description = description,
            progress_image = progress_image
        )
        child_progress.save()
        messages.add_message(request,messages.SUCCESS,f'{child.user_name} {progress_year} years new progress added success')
        return redirect('sadmin:child_progress_list',child_id)

def child_progress_edit_view(request,child_id,progress_id):
    progress = ChildProgress.objects.get(id = int(progress_id))
    context={
        'child_id':child_id,
        'progress':progress
    }
    return render(request,'super-admin/children/progress/progress-edit.html',context)

def child_progress_edit_save(request,child_id,progress_id):
    if request.method == 'POST':
        title = request.POST['progress_title']
        progress_year  = request.POST['progress_year']
        description  = request.POST['description']
        try:
            progress_image = request.FILES['progress_image']
        except:
            progress_image = None
        child = CustomUser.objects.get(id=int(child_id))
        child_progress = ChildProgress.objects.filter(
            id=int(progress_id),
            child_user = child).first()
        child_progress.progress_title = title
        child_progress.progress_description = description
        child_progress.progress_year = progress_year
        if progress_image is not None:
            child_progress.progress_image = progress_image
        child_progress.save()
        messages.add_message(request,messages.SUCCESS,f'{child.user_name} {progress_year} years progress updated success')
        return redirect('sadmin:child_progress_list',child_id)

def child_progress_delete(request,child_id,progress_id):
    progress = ChildProgress.objects.get(id = int(progress_id))
    if progress:
        progress.delete()
        messages.add_message(request,messages.SUCCESS,f'{progress.progress_title} deleted successfully')
        return redirect('sadmin:child_progress_list', child_id)

# child Donate section
def child_donate_list(request,child_id):
    user = CustomUser.objects.get(id = int(child_id))
    donates = Donate.objects.filter(child = user)
    context = {
        'donates':donates,
        'child_id':child_id
    }
    return render(request,'super-admin/children/donate/donate-list.html',context)
def child_donate_add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        per_month = request.POST['per_month']
        duration = request.POST['duration']
        donate_type = request.POST['donate_type']
        occupation = request.POST['occupation']
        address = request.POST['address']
        child_id = request.POST['child_id']
        donate_year = request.POST['donate_year']
        donate = Donate.objects.create(
            child = CustomUser.objects.get(id= int(child_id)),
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            amount = per_month,
            donate_month =duration,
            donate_type = donate_type,
            occupation = occupation,
            address = address,
            donate_year = donate_year
        )
        donate.save()
        messages.add_message(request,messages.SUCCESS,'New donate add successfully')
        return redirect('sadmin:child_donate_list', child_id)
    
def donate_data_get(request):
    if request.method == 'POST':
        donate_id = request.POST['donate_id']
        donate = Donate.objects.filter(id = int(donate_id)).values('first_name',
                                                          'last_name','email',
                                                          'phone_number','amount',
                                                          'donate_month',
                                                          'donate_type',
                                                          'address','occupation',
                                                          'id','donate_year'
                                                          ).first()
        return JsonResponse({'status':'success','data':donate})
    
def donate_edit_data_save(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    per_month = request.POST['per_month']
    duration = request.POST['duration']
    donate_type = request.POST['donate_type']
    occupation = request.POST['occupation']
    address = request.POST['address']
    donate_id = request.POST['donate_id']
    donate_year = request.POST['donate_year']
    donate = Donate.objects.get(id = int(donate_id))
    donate.first_name = first_name
    donate.last_name = last_name
    donate.email = email
    donate.phone_number = phone_number
    donate.amount = per_month
    donate.donate_month =duration
    donate.donate_type = donate_type
    donate.occupation = occupation
    donate.address = address
    donate.donate_year = donate_year
    donate.save()
    messages.add_message(request,messages.SUCCESS,'New donate add successfully')
    return redirect('sadmin:child_donate_list', donate.child.id)

# Start Office staff section
def office_staff_list(request):
    staffs = CustomUser.objects.filter(role = 'STAFF',is_active = True).order_by('-id')
    context = {
        'staffs':staffs
    }
    return render(request,'super-admin/staff/staff-list.html',context)

def office_staff_add_view(request):
    ranks = Rank.objects.all().order_by('rank_name')
    context = {
        'ranks':ranks
    }
    return render(request,'super-admin/staff/staff-add.html',context)

def office_staff_add(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        user_name = request.POST['user_name']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email_address']
        staff_image = request.FILES['staff_image']
        staff_rank = request.POST['rank']

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
            custom_user = CustomUser.objects.get(email = email_address)
            rank = StaffRank.objects.create(
                strank_user = custom_user,
                strank_level = Rank.objects.get(id = int(staff_rank)),
                strank_start_date = date.today()
            )
            rank.save()
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
        select_rank = request.POST['rank']

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
        staff_rank = StaffRank.objects.filter(strank_user = custom_user).last()
        if staff_rank and staff_rank.strank_level.id != int(select_rank):
            staff_rank.strank_end_date = date.today()
            staff_rank.save()
            new_rank = StaffRank.objects.create(
                strank_user = custom_user,
                strank_level = Rank.objects.get(id = int(select_rank)),
                strank_start_date = date.today() + timedelta(days=1)
            )
            new_rank.save()
        else:
            new_rank = StaffRank.objects.create(
                strank_user = custom_user,
                strank_level = Rank.objects.get(id = int(select_rank)),
                strank_start_date = date.today()
            )
            new_rank.save()
        messages.add_message(request,messages.SUCCESS,'Staff profile update successfully')
        return redirect('sadmin:office_staff_list')
    
def staff_get(request):
    if request.method == 'POST':
        staff_id = request.POST['staff']
        user = CustomUser.objects.filter(id = int(staff_id)).values('id','user_name','email').first()
        profile = StaffProfile.objects.filter(staff_user__id= int(staff_id)).values('staff_full_name','staff_phone_number','staff_image').first()
        ranks = Rank.objects.all().values('id','rank_name')
        custom_user =CustomUser.objects.get(id =int(staff_id))
        last_level = StaffRank.objects.filter(strank_user = custom_user).last()
        if last_level:
            user_last_level = last_level.strank_level.id
        else:
            user_last_level = 0
        return JsonResponse({'status':"success","userstaff":user,"staffProfile":profile,"ranks":list(ranks),"user_last_level":user_last_level},safe=False) 

def staff_delete(request,staff_id):
    user_active_status_change = CustomUser.objects.filter(id = staff_id).update(
        is_active = False
    )
    if user_active_status_change:
        messages.add_message(request,messages.SUCCESS,'Staff Account deleted')
        return redirect('sadmin:office_staff_list')
    
# End Office staff section
# start image slide section
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
        slide_image_show = Image.open(slide_image)
        image_width,image_height = slide_image_show.size
        image_aspect_ratio = image_height/image_width
        if image_aspect_ratio >= 0.49 and image_aspect_ratio <= 0.59:
            fs = FileSystemStorage()
            slider = Slider.objects.create(
                slider_caption = slide_title,
                slider_image = fs.save(f'slider/{date.today()}/image-{utlis.date_to_str()}.jpg',slide_image),
                slider_description = slide_description
            )
            if slider:
                messages.add_message(request,messages.SUCCESS,'new slide created successfully')
        else:
            messages.add_message(request,messages.WARNING,'Please slider image size 1220X600 pixels,try again')
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
            slide_image_show = Image.open(slide_image)
            image_width,image_height = slide_image_show.size
            image_aspect_ratio = image_height/image_width
            if image_aspect_ratio >= 0.49 and image_aspect_ratio <= 0.59:
                fs = FileSystemStorage()
                slider.slider_image = fs.save(f'slider/{date.today()}/image-{utlis.date_to_str()}.jpg',slide_image)
            else:
                messages.add_message(request,messages.WARNING,'Please slider image size 1220X600 pixels,try again')
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
def slider_image_delete(request,image_id):
    slide = Slider.objects.get(id = image_id)
    if slide:
        slide.delete()
        messages.add_message(request,messages.SUCCESS,'Gallery image deleted successfully')
    else:
        messages.add_message(request,messages.WARNING,'Gallery image not Found')
    return redirect('sadmin:slider_image_list')
# end image slide section
# video view section
def video_list(request):
    # sliders = Slider.objects.all().order_by('slider_status')
    # context = {
    #     'sliders' : sliders
    # }
    return render(request,'super-admin/video/video-list.html')


# Start child Sponsor section 
def child_sponsor_list_view(request):
    sponsors = SponsorCall.objects.all().order_by('spcall_status')
    
    context = {
        'sponsors':sponsors
    }
    return render(request,'super-admin/child-sponsor/child-sponsor-list.html',context)

def sponsor_detail_view(request):
    return render(request,'super-admin/child-sponsor/child-sponsor-detail.html')

def sponsor_request_accept(request,request_id):
    sponsor_call = SponsorCall.objects.get(id = int(request_id))
    if sponsor_call:
        sponsor_call.spcall_status = 1
        sponsor_call.save()
        messages.add_message(request,messages.SUCCESS,f'{sponsor_call.spcall_first_name} {sponsor_call.spcall_last_name} sponsor request approved successfully')
    else:
        messages.add_message(request,messages.SUCCESS,'Your request invalid')
    return redirect('sadmin:child_sponsor_list_view')
def sponsor_request_cancel(request,request_id):
    sponsor_call = SponsorCall.objects.get(id = int(request_id))
    if sponsor_call:
        sponsor_call.spcall_status = 2
        sponsor_call.save()
        messages.add_message(request,messages.SUCCESS,f'{sponsor_call.spcall_first_name} {sponsor_call.spcall_last_name} sponsor request cancel successfully')
    else:
        messages.add_message(request,messages.SUCCESS,'Your request invalid')
    return redirect('sadmin:child_sponsor_list_view')
# End child Sponsor section 
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
def contact_request_accept(request,request_id):
    contact_ = UserContact.objects.get(id = int(request_id))
    if contact_:
        contact_.uc_status = 1
        contact_.save()
        messages.add_message(request,messages.SUCCESS,f'{contact_.first_name} {contact_.last_name} sponsor request approved successfully')
    else:
        messages.add_message(request,messages.SUCCESS,'Your request invalid')
    return redirect('sadmin:contact_information_list')
def contact_request_cancel(request,request_id):
    contact_ = UserContact.objects.get(id = int(request_id))
    if contact_:
        contact_.uc_status = 2
        contact_.save()
        messages.add_message(request,messages.SUCCESS,f'{contact_.first_name} {contact_.last_name} sponsor request cancel successfully')
    else:
        messages.add_message(request,messages.SUCCESS,'Your request invalid')
    return redirect('sadmin:contact_information_list')
# Start Gallery Image section
def gallery_image_list(request):
    images = GalleryImage.objects.all().order_by('-image_status')
    context = {
        'images':images
    }
    return render(request,'super-admin/gallery/gallery-image-list.html',context)
def gallery_image_save(request):
    if request.method == 'POST':
        photo_title = request.POST['photo_title']
        photo_description = request.POST['photo_description']
        photo_image = request.FILES['photo_image']
        image_show = Image.open(photo_image)
        image_width,image_height = image_show.size
        fs = FileSystemStorage()
        if image_width >= 600 and image_height >= 600:

            gallery_image = GalleryImage.objects.create(
                image_title = photo_title,
                image_description = photo_description,
                gallery_image = fs.save('gallery/image-'+utlis.date_to_str()+".jpg",photo_image)
            )
            gallery_image.save()
            messages.add_message(request,messages.SUCCESS,'Gallery new image added successfully')
        else:
            messages.add_message(request,messages.WARNING,'please gallery image minimum size 600X600 pixel and try again')
        return redirect('sadmin:gallery_image_list')

def gallery_image_edit(request):
    if request.method == 'POST':
        gallery_image_id = request.POST['gallery_image_id']
        image_title = request.POST['image_title']
        image_description = request.POST['image_description']
        try:
            gallery_image = request.FILES['eidt_gallery_image']
        except:
            gallery_image = None
        gallery = GalleryImage.objects.get(id = int(gallery_image_id))
        gallery.image_title = image_title
        gallery.image_description = image_description
        if gallery_image is not None:
            image_show = Image.open(gallery_image)
            image_width,image_height = image_show.size
            fs = FileSystemStorage()
            if image_height >= 600 and image_width >= 600:
                gallery.gallery_image = fs.save('gallery/image-'+utlis.date_to_str()+".jpg",gallery_image)
            else:
                messages.add_message(request,messages.WARNING,'please gallery image minimum size 600X600 pixel and try again')
        if gallery:
            gallery.save()
            messages.add_message(request,messages.SUCCESS,' slide image update successfully')
            return redirect('sadmin:gallery_image_list')


def gallery_image_status_change(request,image_id):
    image = GalleryImage.objects.get(id = image_id)

    if image.image_status == True:
        image.image_status = False
    else:
        image.image_status = True
    
    image.save()
    messages.add_message(request,messages.SUCCESS,'Gallery image status change successfully')
    return redirect("sadmin:gallery_image_list")
def gallery_image_get(request):
    if request.method == 'POST':
        image_id = request.POST['image_id']
        gallery_image = GalleryImage.objects.filter(id = int(image_id)).values('id','image_title','gallery_image','image_description').first()
        return JsonResponse({"status":"success",'gallery_image':gallery_image},safe=True)
def gallery_image_delete(request,image_id):
    gallery_image= GalleryImage.objects.get(id = image_id)
    if gallery_image:
        gallery_image.delete()
        messages.add_message(request,messages.SUCCESS,'Gallery image deleted successfully')
    else:
        messages.add_message(request,messages.WARNING,'Gallery image not Found')
    return redirect('sadmin:gallery_image_list')
# End Gallery Image section

# video gallery section
def video_gallery_list(request):
    videos = VideoGallery.objects.all().order_by('-created_at')
    context={
        'videos':videos
    }
    return render(request,'super-admin/video-gallery/gallery-video-list.html',context)

def video_add(request):
    if request.method == 'POST':
        video_title = request.POST['video_title']
        video_description = request.POST['video_description']
        video_link = request.POST['video_link']

        video = VideoGallery.objects.create(
            video_title = video_title,
            video_description = video_description,
            video_link = video_link
        )
        video.save()
        messages.add_message(request,messages.SUCCESS,'new vedio add successfully')
        return redirect('sadmin:video_gallery_list')
    
def gallery_video_get(request):
    if request.method == 'POST':
        video_id = request.POST['video_id']
        video = VideoGallery.objects.filter(id = int(video_id)).values(
            'id','video_title','video_description','video_link'
        ).first()
        return JsonResponse({'status':'success','video':video})
    
def video_update_save(request):
    if request.method == 'POST':
        video_id = request.POST['gallery_video_id']
        video_title = request.POST['video_title']
        video_description = request.POST['video_description']
        video_link = request.POST['video_link']
        video = VideoGallery.objects.get(id = int(video_id))
        video.video_title = video_title
        video.video_description = video_description
        video.video_link = video_link
        video.save()
        messages.add_message(request,messages.SUCCESS,'Vedio Update successfully')
        return redirect('sadmin:video_gallery_list')