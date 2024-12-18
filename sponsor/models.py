from django.db import models
from user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save
from django.shortcuts import get_object_or_404
from datetime import date
# Create your models here.

class Sponsoranager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        result =  super().get_queryset(*args, **kwargs)
        return result.filter(role = CustomUser.Role.SPONSOR)
class Sponsor(CustomUser):
    base_role = CustomUser.Role.SPONSOR
    staff = Sponsoranager()
    class Meta:
        proxy = True
@receiver(post_save,sender = Sponsor)
def create_sponsor_profile(sender,instance,created,*args, **kwargs):
    if created and instance.role == "SPONSOR":
        SponsorProfile.objects.create(sponsor_user = instance)



class SponsorProfile(models.Model):
    sponsor_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    sponsor_first_name = models.CharField(max_length=250,null=True,blank=True)
    sponsor_last_name = models.CharField(max_length=250,null=True,blank=True)
    sponsor_phone_number = models.CharField(max_length=11,null=True,blank=True)
    sponsor_image = models.ImageField(upload_to=f'sponsor/',null=True,blank=True)
    sponsor_child_request = models.IntegerField(null=True,blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sponsor_user.email
    def save(self,*args, **kwargs):
        if self.id:
            existing = get_object_or_404(SponsorProfile,id = self.id)
            if existing.sponsor_image != self.sponsor_image:
                existing.sponsor_image.delete(save=False)
        super(SponsorProfile,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = 'sponsor.SponsorProfile')
    def sponsor_profile_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'sponsor_image':

                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)


# 0 = Request
# 1 = Approved
# 2 = Cancel
class SponsorCall(models.Model):
    spcall_email = models.EmailField()
    spcall_first_name = models.CharField(max_length=150)
    spcall_last_name = models.CharField(max_length=150)
    spcall_phone_number = models.CharField(max_length=11)
    spcall_number_child = models.IntegerField(null=True,blank=True)
    spcall_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.spcall_email
    

class Donate(models.Model):
    child = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    occupation = models.CharField(max_length=50)
    donate_type = models.CharField(max_length=50)
    donate_month = models.PositiveIntegerField(null=True,blank=True)
    amount = models.PositiveIntegerField()
    donate_year = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    @property
    def total_amount(self):
        return self.donate_month*self.amount
    