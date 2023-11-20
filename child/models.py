from django.db import models
from user.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save
from django.shortcuts import get_object_or_404
from datetime import date
# Create your models here.

class ChildManager(models.Manager):
    def get_queryset(self,*args, **kwargs):
        result =  super().get_queryset(*args, **kwargs)
        return result.filter(role = CustomUser.Role.CHILD)
class Child(CustomUser):
    base_role = CustomUser.Role.CHILD
    child = ChildManager()
    class Meta:
        proxy = True
@receiver(post_save,sender = Child)
def create_child_profile(sender,instance,created,*args, **kwargs):
    if created and instance.role == "CHILD":
        ChildProfile.objects.create(child_user = instance)



class ChildProfile(models.Model):
    child_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    child_first_name = models.CharField(max_length=250,null=True,blank=True)
    child_last_name = models.CharField(max_length=250,null=True,blank=True)
    child_phone_number = models.CharField(max_length=11,null=True,blank=True)
    child_image = models.ImageField(upload_to=f'children/{date.today()}/',null=True,blank=True)
    child_father_name = models.CharField(max_length=250,null=True,blank=True)
    child_mother_name = models.CharField(max_length=250,null=True,blank=True)
    child_date_of_birth = models.DateField(null=True,blank=True)
    child_birth_certificate_number = models.CharField(max_length=250,unique=True,null=True,blank=True)
    child_blood = models.CharField(max_length=250,null=True,blank=True)
    child_weight = models.FloatField(null=True,blank=True)
    child_height = models.FloatField(null=True,blank=True)
    child_present_address = models.TextField(null=True,blank=True)
    child_parmanent_address = models.TextField(null=True,blank=True)
    child_description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.child_user.email
    def save(self,*args, **kwargs):
        if self.id:
            existing = get_object_or_404(ChildProfile,id = self.id)
            if existing.child_image != self.child_image:
                existing.child_image.delete(save=False)
        super(ChildProfile,self).save(*args, **kwargs)

    @receiver(pre_delete,sender = 'child.ChildProfile')
    def child_profile_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'child_image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)