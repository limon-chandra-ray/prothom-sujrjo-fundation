from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from datetime import date,datetime
# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=250)
    event_image = models.ImageField(upload_to=f'event/{date.today()}/')
    event_date = models.DateField()
    event_time = models.TimeField()
    event_status = models.BooleanField()
    event_type = models.CharField(max_length=40)
    event_description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_title
    
    def save(self,*args, **kwargs):
        if self.id:
            event_existing = Event.objects.get(id = self.id)
            if event_existing.event_image != self.event_image:
                event_existing.event_image.delete(save=False)
        super(Event,self).save(*args, **kwargs)

    @receiver(pre_delete,sender="psf.Event")
    def event_image_update_signal(sender,instance,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'event_image':
                p_image = getattr(instance,field.name)
                if p_image:
                    p_image.delete(save=False)

class TeamMember(models.Model):
    tm_name = models.CharField(max_length=250,unique=True)
    tm_email = models.EmailField(unique=True)
    tm_phone = models.CharField(max_length=11,unique=True)
    tm_image = models.ImageField(upload_to=f'team-member/{date.today()}/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tm_name
    
    def save(self,*args, **kwargs):
        if self.id:
            team_member_existing = TeamMember.objects.get(id = self.id)
            if team_member_existing.tm_image != self.tm_image:
                team_member_existing.tm_image.delete(save=False)
        super(TeamMember,self).save(*args, **kwargs)

    @receiver(pre_delete,sender="psf.TeamMember")
    def tm_image_update_signal(sender,instance,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'tm_image':
                p_image = getattr(instance,field.name)
                if p_image:
                    p_image.delete(save=False)
class Rank(models.Model):
    rank_name = models.CharField(max_length=50,unique=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rank_name

class MemberRank(models.Model):
    mr_team_member = models.ForeignKey(TeamMember,on_delete=models.CASCADE)
    mr_level = models.ForeignKey(Rank,on_delete=models.SET_NULL,null=True,blank=True)
    mr_start_date = models.DateField(null=True,blank=True)
    mr_end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mr_team_member.rank_name
    
class ShelterChild(models.Model):
    child_name = models.CharField(max_length=250)
    child_full_name = models.CharField(max_length=250)
    child_image = models.ImageField(upload_to=f'shelter-child/{date.today()}/')
    child_father_name = models.CharField(max_length=250)
    child_mother_name = models.CharField(max_length=250)
    child_date_of_birth = models.DateField()
    child_birth_certificate_number = models.CharField(max_length=250,unique=True)
    child_blood = models.CharField(max_length=250)
    child_weight = models.FloatField()
    child_height = models.FloatField()
    child_present_address = models.TextField()
    child_parmanent_address = models.TextField()
    child_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.child_name
    def save(self,*args, **kwargs):
        if self.id:
            shelter_child_existing = ShelterChild.objects.get(id = self.id)
            if shelter_child_existing.child_image != self.child_image:
                shelter_child_existing.child_image.delete(save=False)
        super(ShelterChild,self).save(*args, **kwargs)

    @receiver(pre_delete,sender="psf.ShelterChild")
    def child_image_update_signal(sender,instance,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'child_image':
                p_image = getattr(instance,field.name)
                if p_image:
                    p_image.delete(save=False)

    @property
    def age(self):
        return int((datetime.now().date() - self.child_date_of_birth).days / 365.25)
class ChildProgress(models.Model):
    cp_child = models.ForeignKey(ShelterChild,on_delete=models.CASCADE)
    cp_education = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Slider(models.Model):
    slider_caption = models.CharField(max_length=250)
    slider_image = models.ImageField(upload_to=f'slider/{date.today()}/')
    slider_description = models.TextField(null=True,blank=True)
    slider_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.slider_caption
    def save(self,*args, **kwargs):
        if self.id:
            shelter_child_existing = Slider.objects.get(id = self.id)
            if shelter_child_existing.slider_image != self.slider_image:
                shelter_child_existing.slider_image.delete(save=False)
        super(Slider,self).save(*args, **kwargs)

    @receiver(pre_delete,sender="psf.Slider")
    def slider_image_update_signal(sender,instance,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'slider_image':
                p_image = getattr(instance,field.name)
                if p_image:
                    p_image.delete(save=False)

class Document(models.Model):
    document_caption = models.CharField(max_length=250)
    document_video = models.FileField(upload_to=f'document/{date.today()}/')
    document_description = models.TextField(null=True,blank=True)
    document_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.document_caption
    
    def save(self,*args, **kwargs):
        if self.id:
            shelter_child_existing = Document.objects.get(id = self.id)
            if shelter_child_existing.document_video != self.document_video:
                shelter_child_existing.document_video.delete(save=False)
        super(Document,self).save(*args, **kwargs)

    @receiver(pre_delete,sender="psf.Document")
    def document_video_update_signal(sender,instance,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'document_video':
                p_image = getattr(instance,field.name)
                if p_image:
                    p_image.delete(save=False)


class UserContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    title = models.CharField(max_length=250)
    contact_message = models.TextField()
    uc_status =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.title
    
    

    