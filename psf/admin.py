from django.contrib import admin
from .models import (
    Event,TeamMember,Rank,MemberRank,
    ShelterChild,ChildProgress,Slider,Document,VideoGallery
)
# Register your models here.

admin.site.register(Event)
admin.site.register(ShelterChild)
admin.site.register(Slider)
admin.site.register(Document)
admin.site.register(Rank)
admin.site.register(VideoGallery)