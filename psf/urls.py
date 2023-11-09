from django.urls import path
app_name = 'psf'
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('donate',views.donate_view,name='donate_view'),
    path('sponsor',views.sponsor_view,name='sponsor_view')
]
# event links
urlpatterns +=[
    path('current-event',views.current_event,name='current_event'),
    path('complete-event',views.complete_event,name='complete_event'),
    path('global-giving-event',views.global_giving_event,name='global_giving_event'),
]

# shelter home links
urlpatterns +=[
    path('about-shelter-home',views.about_shelter_home,name='about_shelter_home'),
    path('children-at-our-shelter-home',views.children_shelter_home,name='children_shelter_home'),
]

# about us links
urlpatterns += [
    path('about-us/org-team',views.org_team,name='org_team'),
    path('about-us/faq',views.faq,name='faq'),
    path('about-us/contact-us',views.contact_us,name='contact_us'),
    path('about-us/about-organization',views.about_org,name='about_org'),
]

# update links
urlpatterns +=[
    path('update/blogs',views.blog,name='blog'),
    path('update/annual-reports',views.annual_report,name='annual_report'),
    path('update/org-news',views.org_new,name='org_new'),
]