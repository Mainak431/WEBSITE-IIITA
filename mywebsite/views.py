from django.shortcuts import render, render_to_response, redirect, get_object_or_404

from .models import *

from django.utils import timezone

from django.contrib.auth import logout, update_session_auth_hash

from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import Group, User

from django.urls import reverse

from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
import datetime
from django.utils.timezone import utc
from .models import department
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .mixins import *
from django.core.mail import EmailMessage


class home(SuccessMessageMixin, LoginView):
    template_name = "index.html"
    success_message = "Login Successful"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['dept_visible'] = "invisible"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_department(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "%(Dept_name)s Department added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = department
    fields = ['Dept_ID', 'Dept_name']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Department added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class update_department(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "%(Dept_name)s Department updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = department
    fields = ['Dept_ID', 'Dept_name']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Department Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class delete_department(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "%(Dept_name)s Department deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = department
    fields = ['Dept_ID', 'Dept_name']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete Department"
        context['alert'] = "Department deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_department, self).delete(request, *args, **kwargs)

class contact_us(SuccessMessageMixin, CreateView):
    template_name = "index.html"
    success_message = "Your Message is saved sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contact
    fields = ['email', 'phone_number', 'Message']

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = "Your Message Saved Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['login'] = True
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        Body = 'Your Message :' + self.object.Message + '.  We will try to revert at the earliest.'
        email = EmailMessage('#IIITA We recieved your message', Body, to=[self.object.email])
        email.send()


        return super(contact_us, self).form_valid(form)


class all_messages(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = "index.html"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contact
    fields = ['email', 'phone_number', 'Message']
    paginate_by = 20


    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Contact.objects.filter(status=True).order_by('-id')
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = "Your Message Saved Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = False
        context['contacts'] = Contacts.objects.all()
        context['boolj'] = True
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class all_contacts(SuccessMessageMixin, ListView):
    template_name = "index.html"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contacts
    fields = ['Name', 'designation', 'email_id', 'phone_number']
    paginate_by = 20

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = "Your Message Saved Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = False
        context['boolc'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class contact(SuccessMessageMixin, ListView):
    template_name = "index.html"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contacts
    fields = ['Name', 'designation', 'email_id', 'phone_number']
    paginate_by = 20

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = ""
        context['object_list'] = Contacts.objects.filter(id=self.kwargs['pk'])
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = False
        context['boolc'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class add_contact(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Contact Information of %(Name)s is added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contacts
    fields = ['Name', 'designation', 'email_id', 'phone_number']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Contact added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class update_contact(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Contact Information of %(Name)s is updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contacts
    fields = ['Name', 'designation', 'email_id', 'phone_number']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Contact Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class delete_contact(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "Contact Information of %(Name)s is deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Contacts
    fields = ['Name', 'designation', 'email_id', 'phone_number']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete Contact"
        context['alert'] = "Contact deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_contact, self).delete(request, *args, **kwargs)

class upload_logo(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Logo updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Logo
    fields = ['logo']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Logo added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class upload_photo(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "One photo with title %(title)s is added to the Gallery sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Photo_gallery
    fields = ['title', 'description', 'photo']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Image added to gallery successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class Show_photo(SuccessMessageMixin, ListView):
    template_name = "index.html"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Photo_gallery
    fields = ['title', 'description', 'photo']
    paginate_by = 20

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = ""
        context['object_list'] = Photo_gallery.objects.filter(id=self.kwargs['pk'])
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = False
        context['boolshow'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_navigation(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "One Navigation Bar named %(name)s added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Navigation_head
    fields = ['name']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Navigation Bar added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class delete_navigation(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "Navigation Bar named %(name)s deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Navigation_head
    fields = ['name']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This Navigation Bar"
        context['alert'] = "Navigation Bar deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_navigation, self).delete(request, *args, **kwargs)

class add_nav(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Navigation link added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Navigation
    fields = ['name', 'links']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Navigation Link added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nav_bar = Navigation_head.objects.filter(id=self.kwargs['pk'])[0]
        return super(add_nav, self).form_valid(form)


class del_nav(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "Navigation Link deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Navigation

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This Link "
        context['alert'] = "Link deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(del_nav, self).delete(request, *args, **kwargs)

class update_nav(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Navigation Link updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Navigation
    fields = ['name', 'links']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Link Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_video(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Video titled %(title)s is added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Videos
    fields = ['title','link','description']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Video added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_file(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "File for %(name)s added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Downloads
    fields = ['name', 'file']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Document added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class del_file(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "File for %(name)s deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Downloads

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This File "
        context['alert'] = "File deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(del_file, self).delete(request, *args, **kwargs)

class update_file(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "File for %(name)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Downloads
    fields = ['name', 'file']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "File Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_announ(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Announcement with Heading %(heading)s added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Announ
    fields = ['heading', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Announcement added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class update_announ(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Announcement with Heading %(heading)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Announ
    fields = ['heading', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Announcement Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class deactivate_announ(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Announcement with Heading %(heading)s deactivated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Announ
    fields = []

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DEACTIVATE"
        context['text'] = "Sure Wanna Deactivate This Announcement "
        context['alert'] = "Announcement Deactivated successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['movebar'] = MovingBar.objects.all()
        context['portal'] = Portal.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.active = False
        return super(deactivate_announ, self).form_valid(form)


class add_portal(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Portal added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Portal
    fields = ['name', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Portal added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['movebar'] = MovingBar.objects.all()
        context['portal'] = Portal.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class update_portal(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Portal updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Portal
    fields = ['name', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Portal Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class delete_portal(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "Portal deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Portal

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete Portal"
        context['alert'] = "Portal deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_portal, self).delete(request, *args, **kwargs)

class add_bar(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Moving Bar Element added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = MovingBar
    fields = ['name', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Moving Bar Element added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['movebar'] = MovingBar.objects.all()
        context['portal'] = Portal.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class update_bar(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Moving Bar Element named %(name)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = MovingBar
    fields = ['name', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Moving Bar Element Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class delete_bar(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "Moving Bar Element named %(name)s deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = MovingBar

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete this element"
        context['alert'] = "Movebar element deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_bar, self).delete(request, *args, **kwargs)

class add_event(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Event %(title)s added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Events
    fields = ['title', 'link', 'Image', 'description']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Event added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['event'] = Events.objects.filter(active=True)
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class update_event(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Event %(title)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Events
    fields = ['title', 'link', 'Image', 'description']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Event Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class deactivate_event(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Event %(title)s deactivated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Events
    fields = []

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DEACTIVATE"
        context['text'] = "Sure Wanna Deactivate This Event "
        context['alert'] = "Event Deactivated successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['movebar'] = MovingBar.objects.all()
        context['portal'] = Portal.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.active = False
        return super(deactivate_event, self).form_valid(form)


class add_section(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "A New Section named %(title)s added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Section
    fields = ['title', 'section_size', 'has_image', 'base_img']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Section added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class update_section(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "Section %(title)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Section
    fields = ['title', 'section_size', 'has_image', 'base_img']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Section Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class delete_section(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "Section %(title)s deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Section
    fields = []

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete Section"
        context['alert'] = "Section deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(delete_section, self).delete(request, *args, **kwargs)

class add_seclink(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "One link added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = SectionLinks
    fields = ['name', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Link added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.section = Section.objects.filter(id=self.kwargs['pk'])[0]
        return super(add_seclink, self).form_valid(form)


class del_seclink(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "One Link deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = SectionLinks

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This Link "
        context['alert'] = "Link deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(del_seclink, self).delete(request, *args, **kwargs)

class update_seclink(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "One Link updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = SectionLinks
    fields = ['name', 'link']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Link Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_secimage(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "One Image added sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = SectionPhotos
    fields = ['title', 'image', 'description']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "ADD"
        context['alert'] = "Image added successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['logo'] = Logo.objects.all().last()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.section = Section.objects.filter(id=self.kwargs['pk'])[0]
        return super(add_secimage, self).form_valid(form)


class del_secimage(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "index.html"
    success_message = "One Image deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = SectionPhotos

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This Photo "
        context['alert'] = "Photo deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(del_secimage, self).delete(request, *args, **kwargs)

class update_secimage(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "index.html"
    success_message = "One Image updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = SectionPhotos
    fields = ['title', 'image', 'description']

    def get_success_url(self):
        return '/accounts/profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Image Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class all_images(SuccessMessageMixin, ListView):
    template_name = "gallery.html"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Photo_gallery
    fields = ['title', 'description', 'photo']
    paginate_by = 20

    def get_success_url(self):
        return '/all_images/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = "Your Message Saved Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = False
        context['contacts'] = Contacts.objects.all()
        context['boolj'] = True
        context['dept_visible'] = "invisible"
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class del_image(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "gallery.html"
    success_message = "Image %(title)s deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Photo_gallery

    def get_success_url(self):
        return '/all_images/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This Photo "
        context['alert'] = "Photo deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(del_image, self).delete(request, *args, **kwargs)

class update_image(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "gallery.html"
    success_message = "Image %(title)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Photo_gallery
    fields = ['title', 'description', 'photo']

    def get_success_url(self):
        return '/all_images/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Image Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['boolimg'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class all_video(SuccessMessageMixin, ListView):
    template_name = "video_gallery.html"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Videos
    fields = ['title', 'description', 'link']
    paginate_by = 20

    def get_success_url(self):
        return '/all_videos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = "Video Saved Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = False
        context['contacts'] = Contacts.objects.all()
        context['boolj'] = True
        context['dept_visible'] = "invisible"
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        return context


class del_video(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = "video_gallery.html"
    success_message = "Video %(title)s deleted sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Videos

    def get_success_url(self):
        return '/all_videos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "DELETE"
        context['text'] = "Sure Wanna Delete This Video "
        context['alert'] = "Video deleted successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(del_video, self).delete(request, *args, **kwargs)

class update_video(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = "video_gallery.html"
    success_message = "Video %(title)s updated sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = Videos
    fields = ['title', 'description', 'link']

    def get_success_url(self):
        return '/all_videos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "UPDATE"
        context['text'] = "UPDATE"
        context['alert'] = "Video Updated Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()

        return context


class add_reply(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = "index.html"
    success_message = "Reply Sent sucessfully"
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%H:%M:%S')
    model = add_reply
    fields = ['Subject','Body']

    def get_success_url(self):
        return '/all_messages/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.utcnow().replace(tzinfo=utc)
        context['time'] = datetime.datetime.now().strftime('%H:%M:%S')
        context['dept'] = department.objects.all()
        context['button'] = "SEND"
        context['alert'] = "Reply Sent Successfully"
        context['count_messages'] = Contact.objects.filter(status=True).count()
        context['booli'] = True
        context['contacts'] = Contacts.objects.all()
        context['logo'] = Logo.objects.all().last()
        context['image'] = Photo_gallery.objects.all()
        context['nav_bar'] = Navigation_head.objects.all()
        context['nav'] = Navigation.objects.all()
        context['video'] = Videos.objects.all().last()
        context['Downloads'] = Downloads.objects.all()
        context['Announ'] = Announ.objects.filter(active=True)
        context['portal'] = Portal.objects.all()
        context['event'] = Events.objects.filter(active=True)
        context['section'] = Section.objects.all()
        context['sec_images'] = SectionPhotos.objects.all()
        context['sec_links'] = SectionLinks.objects.all()
        context['movebar'] = MovingBar.objects.all()
        context['login'] = True
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Email = Contact.objects.get(id = self.kwargs['pk']).email
        self.object = form.save(commit=False)
        email = EmailMessage(self.object.Subject, self.object.Body, to=[self.object.Email])
        email.send()
        nc = Contact.objects.get(id=self.kwargs['pk'])
        nc.status = False
        nc.save()
        return super(add_reply, self).form_valid(form)
