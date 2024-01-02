from django.db import models
from user.models import CustomUser
from sadmin.utlis import date_to_str
from django.dispatch import receiver
from django.db.models.signals import pre_delete,post_save
from django.shortcuts import get_object_or_404
from datetime import date,datetime
from PIL import Image
import os
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
def child_image_path(instance,filename):
    file_name,extension = os.path.splitext(filename)
    new_file_path = f"{date_to_str()}{extension}"
    return os.path.join('children',new_file_path)
def child_cover_image_path(instance,filename):
    file_name,extension = os.path.splitext(filename)
    new_file_path = f"{date_to_str()}{extension}"
    return os.path.join('children-cover',new_file_path)

class ChildProfile(models.Model):
    child_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    child_first_name = models.CharField(max_length=250,null=True,blank=True)
    child_last_name = models.CharField(max_length=250,null=True,blank=True)
    child_phone_number = models.CharField(max_length=11,null=True,blank=True)
    child_image = models.ImageField(upload_to=child_image_path,null=True,blank=True)
    child_cover_image = models.ImageField(upload_to=child_cover_image_path,null=True,blank=True)
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
    child_join = models.DateField(null=True,blank=True)
    child_hobbie = models.CharField(max_length = 100,null=True,blank=True)
    child_study = models.CharField(max_length =250,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.child_user.email
    @property
    def age(self):
        today_date = date.today()
        age_date = today_date - self.child_date_of_birth
        return age_date.days // 365
    def save(self,*args, **kwargs):
        if self.id:
            existing = get_object_or_404(ChildProfile,id = self.id)
            if existing.child_image != self.child_image:
                existing.child_image.delete(save=False)
            if existing.child_cover_image != self.child_cover_image:
                existing.child_cover_image.delete(save=False)

        super(ChildProfile,self).save(*args, **kwargs)
        if self.child_image:
            image = Image.open(self.child_image.path)
            image.thumbnail((300,300))
            image.save(self.child_image.path)
        
        if self.child_cover_image:
            image = Image.open(self.child_cover_image.path)
            if image.mode not in ("L", "RGB"):
                image = image.convert("RGB")
            x = 1220
            y = 600
            img_ratio = float(image.size[0]) / image.size[1]

            if x==0.0:
                x = y * img_ratio
            elif y==0.0:
                y = x / img_ratio
            resize_ratio = float(x) / y
            x = int(x); y = int(y)
            if(img_ratio > resize_ratio):
                output_width = x * image.size[1] / y
                output_height = image.size[1]
                originX = image.size[0] / 2 - output_width / 2
                originY = 0
            else:
                output_width = image.size[0]
                output_height = y * image.size[0] / x
                originX = 0
                originY = image.size[1] / 2 - output_height / 2
            cropBox = (originX, originY, originX + output_width, originY + output_height)
            image = image.crop(cropBox)
            image.thumbnail([x, y])
            image.save(self.child_cover_image.path)
    @receiver(pre_delete,sender = 'child.ChildProfile')
    def child_profile_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'child_image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)
    def child_cover_image_delete_signal(instance,sender,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'child_cover_image':
                logo = getattr(instance,field.name)
                if logo:
                    logo.delete(save = False)

def progress_image_path(instance,filename):
    file_name,extension = os.path.splitext(filename)
    new_file_path = f"{date_to_str()}{extension}"
    return os.path.join('child-progress',new_file_path)

class ChildProgress(models.Model):
    child_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    progress_year = models.IntegerField(null=True,blank=True)
    progress_title = models.CharField(max_length=250)
    progress_description = models.TextField(null=True,blank=True)
    progress_image = models.ImageField(upload_to=progress_image_path)
    progress_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.progress_title
    
    def save(self,*args, **kwargs):
        if self.id:
            progess_image_existing = ChildProgress.objects.get(id = self.id)
            if progess_image_existing.progress_image != self.progress_image:
                progess_image_existing.progress_image.delete(save=False)
    
        super(ChildProgress,self).save(*args, **kwargs)
        if self.progress_image:
            image = Image.open(self.progress_image.path)
            image.thumbnail((750,600),Image.BICUBIC)
            image.save(self.progress_image.path)

    @receiver(pre_delete,sender="psf.ChildProgress")
    def progress_image_update_signal(sender,instance,*args, **kwargs):
        for field in instance._meta.fields:
            if field.name == 'progress_image':
                p_image = getattr(instance,field.name)
                if p_image:
                    p_image.delete(save=False)



