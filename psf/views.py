from django.shortcuts import render,redirect
from django.http import JsonResponse
from psf.models import ShelterChild,Slider,Event,GalleryImage
from sponsor.models import Sponsor,SponsorProfile,SponsorCall,Donate
from user.models import CustomUser
from child.models import ChildProfile,ChildProgress
from datetime import date
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from psf.models import ShelterChild,VideoGallery
# Create your views here.

def home(request):
    slides = Slider.objects.filter(slider_status = True).order_by('-id')
    context = {
        'slides':slides
    }
    return render(request,'psf/home/home.html',context)

# event show
def current_event(request):
    current_events = Event.objects.filter(event_status = True, event_date__gte = date.today()).order_by('-id')
    context = {
        'current_events':current_events
    }
    return render(request,'psf/event/current-event.html',context)

def complete_event(request):
    complete_events = Event.objects.filter(event_status = False, event_date__lte = date.today()).order_by('-id')
    context = {
        'complete_events':complete_events
    }
    return render(request,'psf/event/complete-event.html',context)
def global_giving_event(request):
    global_events = Event.objects.filter(event_type='global').order_by('-id')
    context = {
        'global_events':global_events
    }
    return render(request,'psf/event/global-event.html',context)

def event_details(request,event_id):
    event = Event.objects.get(id = int(event_id))
    same_type_events = Event.objects.filter(event_type = event.event_type,event_status = True).exclude(id = int(event_id)).order_by('-id')
    context = {
        'event':event,
        'same_type_events':same_type_events
    }
    return render(request,'psf/event/event_details.html',context)

# shelter home show
def about_shelter_home(request):
    return render(request,'psf/shelter/about-shelter-home.html')
def children_shelter_home(request):
    shelter_children = ChildProfile.objects.all()
    context = {
        'shelter_childrens':shelter_children
    }
    return render(request,'psf/shelter/shelter-home-children.html',context)
def child_details(request, id):
    shelter_child = get_object_or_404(ChildProfile, id=id)
    user = CustomUser.objects.get(id = shelter_child.child_user.id)

    child_progress_years = ChildProgress.objects.filter(child_user = user).values('progress_year').order_by('-progress_year')
    last_year = child_progress_years.first()['progress_year']
    child_progress = ChildProgress.objects.filter(child_user=user,progress_year = last_year).order_by('created_at')
    
    donate_years = Donate.objects.filter(child = user).values('donate_year').order_by('-donate_year')
    last_donate_year = donate_years.first()['donate_year']
    child_doners = Donate.objects.filter(child = user,donate_year=last_donate_year).order_by('created_at')
    context = {
        'shelter_child': shelter_child,
        'child_progress_years':child_progress_years,
        'child_progress':child_progress,
        'last_year':last_year,
        'child_doners':child_doners,
        'last_donate_year':last_donate_year,
        'donate_years':donate_years
    }
    return render(request, 'psf/shelter/child_details.html', context)

def child_progress_change(request):
    if request.method == 'POST':
        user_id = request.POST['child_id']
        user = CustomUser.objects.get(id = int(user_id))
        year = request.POST['year']
        child_progress = ChildProgress.objects.filter(child_user=user,progress_year = int(year)).values('id',
                                                                                        'progress_title',
                                                                                        'progress_description',
                                                                                        'progress_image').order_by('created_at')
        return JsonResponse({"status":"success",'progress':list(child_progress)});

def child_donate_change(request):
    if request.method == 'POST':
        user_id = request.POST['child_id']
        user = CustomUser.objects.get(id = int(user_id))
        year = request.POST['year']
        donates = Donate.objects.filter(child=user,donate_year = int(year)).values('id',
                                                                                        'first_name',
                                                                                        'last_name',
                                                                                        'donate_type',
                                                                                        'created_at',
                                                                                        'occupation'
                                                                                        ).order_by('created_at')
        return JsonResponse({"status":"success",'donates':list(donates)});
# abouts us show
def org_team(request):
    return render(request,'psf/about-us/org-team.html')
def faq(request):
    return render(request,'psf/about-us/faq.html')
def contact_us(request):
    return render(request,'psf/about-us/contact-us.html')
def about_org(request):
    return render(request,'psf/about-us/about-organization.html')

# update show
def blog(request):
    return render(request,'psf/update/blog.html')

def org_new(request):
    return render(request,'psf/update/org-new.html')
def annual_report(request):
    return render (request,'psf/update/annual-report.html')

# gallery view
def gallery_view(request):
    gallery_images = GalleryImage.objects.filter(image_status = True).order_by('-id')[:6]

    context={
        'gallery_images':gallery_images
    }
    return render(request,'psf/gallery/gallery.html',context)
def video_gallery(request):
    video_gallery = VideoGallery.objects.all().order_by('-created_at')[:4]
    context={
        'video_gallery':video_gallery
    }
    return render(request,'psf/gallery/video-gallery.html',context)
# donate view
def donate_view(request):
    return render(request,'psf/donate/donate.html')

# sponser view
def sponsor_view(request):
    return render(request,'psf/sponsor/sponsor.html')

# def sponsor_request(request):
#     if request.method == 'POST':
#         f_name = request.POST['fname']
#         l_name = request.POST['lname']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         number_of_child = request.POST['number_of_child']
#         email_check = CustomUser.objects.filter(email = email).first()
#         if email_check is None:

#             sponsor = Sponsor.objects.create_sponsor(
#                 email = email,
#                 user_name = f_name,
#                 password = phone
#             )
#             sponsor.save()
#             sponsor_profile = SponsorProfile.objects.filter(sponsor_user = sponsor).first()
#             sponsor_profile.sponsor_first_name = f_name
#             sponsor_profile.sponsor_last_name = l_name
#             sponsor_profile.sponsor_phone_number = phone
#             sponsor_profile.sponsor_child_request = number_of_child
#             sponsor_profile.save()
#             messages.add_message(request,messages.SUCCESS,'your sponsor request create successfully')
#         else:
#             messages.add_message(request,messages.WARNING,'your input email already added')
#         return redirect('psf:sponsor_view')

def sponsor_request(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        number_of_child = request.POST['number_of_child']
        sponsor_call = SponsorCall.objects.create(
            spcall_email = email,
            spcall_first_name = f_name,
            spcall_last_name = l_name,
            spcall_phone_number = phone,
            spcall_number_child = number_of_child
        )
        sponsor_call.save()
        messages.add_message(request,messages.SUCCESS,'your sponsor request create successfully')
    else:
        messages.add_message(request,messages.WARNING,'your input email already added')
    return redirect('psf:sponsor_view')

# Error 404 and 500 Handler 
def error_404_view(request,exception):
    return render(request,'notifications/error_404.html')
def error_500_view(request):
    return render(request,'notifications/error_500.html')