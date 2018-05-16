from django.conf.urls import url

from . import views
from .views import *
import django.contrib.auth.urls

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [

                  url('^$', views.home.as_view(), name='home'),
                  url('^accounts/profile/$', views.home.as_view(), name="home"),
                  url('^add_department/$', views.add_department.as_view(), name="add_department"),
                  url(r'^update_department/(?P<pk>\d+)/$', views.update_department.as_view(), name="update_department"),
                  url(r'^delete_department/(?P<pk>\d+)/$', views.delete_department.as_view(), name="delete_department"),
                  url(r'^contact_us/$', views.contact_us.as_view(), name="contact_us"),
                  url(r'^all_messages/$', views.all_messages.as_view(), name="All Messages"),
                  url(r'^all_contacts/$', views.all_contacts.as_view(), name="All Contacts"),
                  url(r'^add_contact/$', views.add_contact.as_view(), name="add_contact"),
                  url(r'^update_contact/(?P<pk>\d+)/$', views.update_contact.as_view(), name="update_contact"),
                  url(r'^contacts/(?P<pk>\d+)/$', views.contact.as_view(), name="contact"),
                  url(r'^delete_contact/(?P<pk>\d+)/$', views.delete_contact.as_view(), name="delete_contact"),
                  url(r'^upload_logo/$', views.upload_logo.as_view(), name="upload_logo"),
                  url(r'^upload_photo/$', views.upload_photo.as_view(), name="upload_photo"),
                  url(r'^show_photo/(?P<pk>\d+)/$', views.Show_photo.as_view(), name="Show Photo"),
                  url(r'^add_navigation/$', views.add_navigation.as_view(), name="add_navigation"),
                  url(r'^delete_navigation/(?P<pk>\d+)/$', views.delete_navigation.as_view(), name="delete_navigation"),
                  url(r'^add_nav/(?P<pk>\d+)/$', views.add_nav.as_view(), name="add_nav"),
                  url(r'^delete_nav/(?P<pk>\d+)/$', views.del_nav.as_view(), name="del_nav"),
                  url(r'^update_nav/(?P<pk>\d+)/$', views.update_nav.as_view(), name="update_nav"),
                  url(r'^add_video/$', views.add_video.as_view(), name="add_video"),
                  url(r'^add_file/$', views.add_file.as_view(), name="add_file"),
                  url(r'^delete_file/(?P<pk>\d+)/$', views.del_file.as_view(), name="del_file"),
                  url(r'^update_file/(?P<pk>\d+)/$', views.update_file.as_view(), name="update_file"),
                  url(r'^add_announ/$', views.add_announ.as_view(), name="add_announ"),
                  url(r'^deactivate_announ/(?P<pk>\d+)/$', views.deactivate_announ.as_view(), name="deactivate_announ"),
                  url(r'^update_announ/(?P<pk>\d+)/$', views.update_announ.as_view(), name="update_announ"),
                  url(r'^add_portal/$', views.add_portal.as_view(), name="add_portal"),
                  url(r'^delete_portal/(?P<pk>\d+)/$', views.delete_portal.as_view(), name="del_portal"),
                  url(r'^update_portal/(?P<pk>\d+)/$', views.update_portal.as_view(), name="update_portal"),
                  url(r'^add_tobar/$', views.add_bar.as_view(), name="add_bar"),
                  url(r'^delete_bar/(?P<pk>\d+)/$', views.delete_bar.as_view(), name="del_bar"),
                  url(r'^update_bar/(?P<pk>\d+)/$', views.update_bar.as_view(), name="update_bar"),
                  url(r'^add_event/$', views.add_event.as_view(), name="add_bar"),
                  url(r'^deactivate_event/(?P<pk>\d+)/$', views.deactivate_event.as_view(), name="deactivate_event"),
                  url(r'^update_event/(?P<pk>\d+)/$', views.update_event.as_view(), name="update_event"),
                  url(r'^add_section/$', views.add_section.as_view(), name="add_section"),
                  url(r'^delete_section/(?P<pk>\d+)/$', views.delete_section.as_view(), name="del_section"),
                  url(r'^update_section/(?P<pk>\d+)/$', views.update_section.as_view(), name="update_section"),
                  url(r'^add_seclink/(?P<pk>\d+)/$', views.add_seclink.as_view(), name="add_seclink"),
                  url(r'^delete_seclink/(?P<pk>\d+)/$', views.del_seclink.as_view(), name="del_seclink"),
                  url(r'^update_seclink/(?P<pk>\d+)/$', views.update_seclink.as_view(), name="update_seclink"),
                  url(r'^add_secimage/(?P<pk>\d+)/$', views.add_secimage.as_view(), name="add_secimage"),
                  url(r'^delete_secimg/(?P<pk>\d+)/$', views.del_secimage.as_view(), name="del_secimage"),
                  url(r'^update_secimg/(?P<pk>\d+)/$', views.update_secimage.as_view(), name="update_secimage"),
                  url(r'^all_images/$', views.all_images.as_view(), name="all_images"),
                  url(r'^delete_photo/(?P<pk>\d+)/$', views.del_image.as_view(), name="del_image"),
                  url(r'^update_photo/(?P<pk>\d+)/$', views.update_image.as_view(), name="update_image"),
                  url(r'^all_videos/$', views.all_video.as_view(), name="all_video"),
                  url(r'^delete_video/(?P<pk>\d+)/$', views.del_video.as_view(), name="del_video"),
                  url(r'^update_video/(?P<pk>\d+)/$', views.update_video.as_view(), name="update_video"),
                  url(r'^add_reply/(?P<pk>\d+)/$', views.add_reply.as_view(), name="add_reply"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
