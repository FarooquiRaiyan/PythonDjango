from django.db import models
from django.contrib.auth.models import User

#important django signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timesince import timesince
from django.utils import timezone
from datetime import timedelta, datetime
from phonenumber_field.modelfields import PhoneNumberField


#profile picture location 
def profile_image_path_location(instance, filename):
    #get todays date YYYY-MM-DD
    today_date=datetime.now().strftime('%Y-%m-%d')
    #return the upload path
    return "profile/%s/%s/%s" % (instance.user.username, today_date,filename)
    
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    job_title = models.CharField(max_length=255, null=True, blank= True)
    profile_picture = models.ImageField(upload_to=profile_image_path_location, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank= True)
    phone=PhoneNumberField(null=True, blank=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    
    @property
    def profile_picture_url(self):
        try:
            image = self.profile_picture.url
        except:
            image = "https://img.freepik.com/free-psd/contact-icon-illustration-isolated_23-2151903337.jpg? t=st=1744395156~exp=1744398756~hmac=25ae78d463f50b9f7172a7528471fb4960728ba380539e1649a41f15979f1e7b&w=826"
        return image
    
    def full_name(self):
        name=self.user.get_full_name()
        if name:
            return name
        return self.user.get_username()
    
    @property
    def date_joined(self):
        time_difference = timezone.now() - self.user.date_joined
        if time_difference <= timedelta(days=2):
            return timesince(self.user.date_joined) + " ago"
        else:
            return self.user.date_joined.strftime('%b %d, %Y')
        
    
    # @property
    # def full_name(self):
    #     first_name=self.user.first_name
    #     last_name=self.user.last_name
    #     if first_name and last_name :
    #         return f"{first_name} {last_name}"
    #     return self.user.username       
    
    

# @receiver(post_save, sender = User)
# def create_user_profile(sender,instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def create_user_profile(sender,instance, **kwargs):
    #if user already exists an there's no profile create a profile
    Profile.objects.get_or_create(user=instance)
    
