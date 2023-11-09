from django.db import models
from user.models import CustomUser
from psf.models import Rank
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save
from django.shortcuts import get_object_or_404
from datetime import date
# Create your models here.

class StaffManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        result =  super().get_queryset(*args, **kwargs)
        return result.filter(role = CustomUser.Role.STAFF)
class Staff(CustomUser):
    base_role = CustomUser.Role.STAFF
    staff = StaffManager()
    class Meta:
        proxy = True
@receiver(post_save,sender = Staff)
def create_staff_profile(sender,instance,created,*args, **kwargs):
    if created and instance.role == "STAFF":
        StaffProfile.objects.create(staff_user = instance)



class StaffProfile(models.Model):
    staff_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    staff_full_name = models.CharField(max_length=250)
    staff_phone_number = models.CharField(max_length=11,unique=True,null=True,blank=True)
    staff_image = models.ImageField(upload_to=f'staff/{date.today()}/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff_user.email
    def save(self,*args, **kwargs):
        if self.id:
            existing = get_object_or_404(StaffProfile,id = self.id)
            if existing.staff_image != self.staff_image:
                existing.staff_image.delete(save=False)
        super(StaffProfile,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = 'staff.StaffProfile')
    def staff_profile_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'staff_image':

                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)
    
class StaffRank(models.Model):
    strank_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    strank_level = models.ForeignKey(Rank,on_delete=models.SET_NULL,null=True,blank=True)
    strank_start_date = models.DateField(null=True,blank=True)
    strank_end_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)