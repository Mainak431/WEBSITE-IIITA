from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User
from model_utils import Choices

class department(models.Model):
    id = models.AutoField(primary_key=True)
    Dept_ID = models.CharField(max_length=20, unique=True, verbose_name="Department ID/Short Name")
    Dept_name = models.CharField(max_length=200, unique=True, verbose_name="Department Name")

    def publish(self):
        self.save()

    def _str_(self):
        return self.D_name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, verbose_name="Email ID (Preferably Personal)")
    phone_regex = RegexValidator(regex=r'^\+\d{1,3}\-\d{10,12}$', \
                                 message="Phone number must be entered in the format: '+91-9830098300'. +91 is the country code of India.")
    phone_number = models.CharField(validators=[phone_regex], default='+91-', max_length=16,
                                    verbose_name='Personal Mobile Number')
    Message = models.TextField(default="Enter your Message Here")
    status = models.BooleanField(default=True,blank=True)


class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30, verbose_name="NAME OF THE PERSON")
    designation = models.CharField(max_length=30, verbose_name="Designation Of the Person")
    email_id = models.EmailField(max_length=50, verbose_name="Email ID (Preferably Personal)")
    phone_regex = RegexValidator(regex=r'^\+\d{1,3}\-\d{10,12}$', \
                                 message="Phone number must be entered in the format: '+91-9830098300'. +91 is the country code of India.")
    phone_number = models.CharField(validators=[phone_regex], default='+91-', max_length=16,
                                    verbose_name='Personal Mobile Number')


class Logo(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to='Logo', verbose_name="Upload The Logo. Preferably in 240px by 240px")


class Photo_gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, verbose_name="Title Of The Image")
    description = models.TextField(default="Enter description about the Image")
    photo = models.ImageField(upload_to='photo_gallery', verbose_name="Upload the Image")


class Navigation_head(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name="Name Of the Navigation Bar")


class Navigation(models.Model):
    id = models.AutoField(primary_key=True)
    nav_bar = models.ForeignKey(Navigation_head, on_delete=models.CASCADE,
                                verbose_name="Existing Navigation Bar Option", null=True)
    links = models.CharField(max_length=100, verbose_name="Link to Add(Include Complete Address)", null=True)
    name = models.CharField(max_length=100, verbose_name="Title for this link(Will be shown in the Nav bar)", null=True)


class Videos(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=100, verbose_name="Embeded Link of the video")
    title = models.CharField(max_length=30,verbose_name="Title of the video you want to specify",null=True)
    description = models.CharField(max_length=30,verbose_name="Description of the video",null=True)


class Downloads(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='documents', verbose_name="Upload the Document")
    name = models.CharField(max_length=20, verbose_name="Name of the Download Element")

class Announ(models.Model):
    id =  models.AutoField(primary_key=True)
    heading = models.CharField(max_length= 100,verbose_name="Provide a heading")
    link = models.CharField(max_length=100,verbose_name="Provide the link to which you want to redirect")
    active = models.BooleanField(default= True,verbose_name="Activate Or Deactivate")

class Portal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name="Provide a Title for this link")
    link = models.CharField(max_length=100,verbose_name="Provide the link of the portal you want to associate it with")

class MovingBar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name="Provide a Title for this link")
    link = models.CharField(max_length=100, verbose_name="Provide the link of the portal you want to associate it with")

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 30,verbose_name= "Provide a Title for this Event")
    link = models.CharField(max_length=100,verbose_name="Provide a link where this event is taking place",null=True,blank=True)
    Image = models.ImageField(upload_to='event_gallery',verbose_name="Its always recommended to add an Image",null=True,blank=True)
    description = models.TextField(default="Enter Details about this event here",verbose_name="Enter description about the event here")
    active = models.BooleanField(default=True,verbose_name="Activate Or Deactivate")

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,verbose_name="Provide a Title for this Section")
    Size = Choices(
        3,4,6,12
      )
    section_size = models.IntegerField(choices=Size,verbose_name="This will specify the width of the section. Enter only from 3 ,4 ,6 and 12.Related to Bootstrap")
    has_image = models.BooleanField(default=False,verbose_name="Check if you want to upload Image in this section or not")
    base_img = models.ImageField(upload_to='section_base_images',verbose_name="This Image will be your carousel base image",null=True,blank=True)

class SectionLinks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name="Name of the link in the page")
    link = models.CharField(max_length=100,verbose_name="Link which leads to  the page")
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True)

class SectionPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=300,verbose_name="Title Of the Image")
    image = models.ImageField(upload_to='section_image',verbose_name="Upload the Image You Want to show",null=True,blank=True)
    description = models.CharField(max_length=50,verbose_name="Enter a small description of the image",blank=True,null=True)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True)


class add_reply(models.Model):
    id = models.AutoField(primary_key=True)
    Subject = models.CharField(max_length=30, verbose_name="Enter the Subject of the Email. This will be your Email Subject")
    Body = models.TextField(default="Message Body Here" ,verbose_name="Body: Your Message will go here")
    Email = models.EmailField(max_length=50,blank=True,null=True)