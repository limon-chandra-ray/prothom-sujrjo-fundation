from django.shortcuts import render, get_object_or_404
from psf.models import ShelterChild
# Create your views here.
def home(request):
    return render(request,'psf/home.html')

# event show
def current_event(request):
    return render(request,'psf/event/current-event.html')
def complete_event(request):
    return render(request,'psf/event/complete-event.html')
def global_giving_event(request):
    return render(request,'psf/event/global-event.html')
def event_details(request):
    return render(request,'psf/event/event_details.html')

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