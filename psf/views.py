from django.shortcuts import render,redirect
from psf.models import ShelterChild,Slider,Event
from sponsor.models import Sponsor,SponsorProfile
from user.models import CustomUser
from datetime import date
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from psf.models import ShelterChild
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

    return render(request,'psf/event/current-event.html')
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
    context = {
        'event':event
    }
    return render(request,'psf/event/event_details.html',context)

# shelter home show
def about_shelter_home(request):
    return render(request,'psf/shelter/about-shelter-home.html')
def children_shelter_home(request):
    shelter_children = ShelterChild.objects.all()
    context = {
        'shelter_childrens':shelter_children
    }
    return render(request,'psf/shelter/shelter-home-children.html',context)
def child_details(request, id):
    shelter_child = get_object_or_404(ShelterChild, id=id)
    context = {
        'shelter_child': shelter_child
    }
    return render(request, 'psf/shelter/child_details.html', context)

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
    return render(request,'psf/gallery/gallery.html')

# donate view
def donate_view(request):
    return render(request,'psf/donate/donate.html')

# sponser view
def sponsor_view(request):
    return render(request,'psf/sponsor/sponsor.html')

def sponsor_request(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        number_of_child = request.POST['number_of_child']
        email_check = CustomUser.objects.filter(email = email).first()
        if email_check is None:

            sponsor = Sponsor.objects.create_sponsor(
                email = email,
                user_name = f_name,
                password = phone
            )
            sponsor.save()
            sponsor_profile = SponsorProfile.objects.filter(sponsor_user = sponsor).first()
            sponsor_profile.sponsor_first_name = f_name
            sponsor_profile.sponsor_last_name = l_name
            sponsor_profile.sponsor_phone_number = phone
            sponsor_profile.sponsor_child_request = number_of_child
            sponsor_profile.save()
            messages.add_message(request,messages.SUCCESS,'your sponsor request create successfully')
        else:
            messages.add_message(request,messages.WARNING,'your input email already added')
        return redirect('psf:sponsor_view')
