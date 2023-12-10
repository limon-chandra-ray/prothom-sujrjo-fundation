from django.contrib import admin
from .models import (
    Event,TeamMember,Rank,MemberRank,
    ShelterChild,ChildProgress,Slider,Document
)
# Register your models here.

admin.site.register(Event)
admin.site.register(ShelterChild)
admin.site.register(Slider)
admin.site.register(Document)
admin.site.register(Rank)