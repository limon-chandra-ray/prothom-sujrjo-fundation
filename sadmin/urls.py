from django.urls import path
from . import views
app_name = 'sadmin'
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    
]

# event urls section
urlpatterns +=[
    path('event-list',views.event_list,name='event_list'),
    path('event-create',views.event_add,name='event_add'),
    path('event-get',views.event_get,name='event_get'),
    path('event-edit',views.event_edit,name='event_edit'),
    path('event-delete-<int:event_id>',views.event_delete,name='event_delete')
]

# children urls section
urlpatterns +=[
    path('children-list',views.children_list,name='children_list'),
    path('children-create',views.children_create_view,name='children_create_view'),
    path('children-create-data-save',views.children_save,name='children_save'),
    path('children-<int:children_id>-details-update',views.children_info_update_view,name='children_info_update_view'),
    path('children-<int:children_id>-save-update',views.children_info_update_save,name='children_info_update_save'),
    path('children-<int:children_id>-delete',views.children_info_delete,name='children_info_delete')

]
# children progress section
urlpatterns +=[
    path('children-<int:child_id>-progress-list',views.child_progress_list,name='child_progress_list'),
    path('children-<int:child_id>-progress-add',views.child_progress_add_view,name='child_progress_add_view'),
    path('children-<int:child_id>-progress-save',views.child_progress_add_save,name='child_progress_add_save'),
    path('children-<int:child_id>-progress-<int:progress_id>-edit',views.child_progress_edit_view,name='child_progress_edit_view'),
    path('children-<int:child_id>-progress-<int:progress_id>-save',views.child_progress_edit_save,name='child_progress_edit_save'),
    path('children-<int:child_id>-progress-<int:progress_id>-delete',views.child_progress_delete,name='child_progress_delete'),
]   
# children donar section
urlpatterns +=[
    path('children-<int:child_id>-donate-list',views.child_donate_list,name='child_donate_list'),
    path('children-donate-add',views.child_donate_add,name='child_donate_add'),
    path('chilfren-donate-data-get',views.donate_data_get,name='donate_data_get'),
    path('chilfren-update-data-save',views.donate_edit_data_save,name='donate_edit_data_save'),
]

# staff urls section
urlpatterns += [
    path('staff-list',views.office_staff_list,name='office_staff_list'),
    path('staff-member-add',views.office_staff_add_view,name='office_staff_add_view'),
    path('staff-member-save',views.office_staff_add,name='office_staff_add'),
    path('staff-member-edit',views.office_staff_edit,name='office_staff_edit'),
    path('staff-get-info',views.staff_get,name='staff_get'),
    path('staff-member-delete-<int:staff_id>',views.staff_delete,name='staff_delete'),
]


# slider image urls section
urlpatterns += [
    path('slider-image-list',views.slider_image_list,name='slider_image_list'),
    path('slider-image-add',views.slider_image_add,name='slider_image_add'),
    path('slider-image-edit',views.slider_image_edit,name='slider_image_edit'),
    path('slider-image-<int:image_id>-status-change',views.slider_image_status_change,name='slider_image_status_change'),
    path('slide-get',views.get_slide,name='get_slide'),
    path('slid-image-<int:image_id>-delete',views.slider_image_delete,name='slider_image_delete')
]


# sponsor urls section
urlpatterns +=[
    path('sponsor-list',views.child_sponsor_list_view,name='child_sponsor_list_view'),
    path('sponsor-<int:request_id>-request-approve',views.sponsor_request_accept,name='sponsor_request_accept'),
    path('sponsor-<int:request_id>-request-cancel',views.sponsor_request_cancel,name='sponsor_request_cancel')
]

# authentication system section
urlpatterns +=[
    path('log-in',views.login_view,name='login_view'),
    path('change-password',views.change_password_view,name='change_password_view'),
    path('log-out',views.super_admin_logout,name='super_admin_logout'),
    path('edit-profile',views.edit_profile_view,name='edit_profile_view'),
    path('edit-profile-save',views.edit_profile_save,name='edit_profile_save')
]

# contact us section
urlpatterns +=[
    path('contact-information-save',views.contact_information_save,name='contact_information_save'),
    path('contact-information-list',views.contact_information_list,name='contact_information_list'),
    path('contact-<int:request_id>-request-approve',views.contact_request_accept,name='contact_request_accept'),
    path('contact-<int:request_id>-request-cancel',views.contact_request_cancel,name='contact_request_cancel')
]

#Gallery Image section
urlpatterns +=[
    path('gallery-image-list',views.gallery_image_list,name='gallery_image_list'),
    path('gallery-image-add',views.gallery_image_save,name='gallery_image_save'),
    path('gallery-image-<int:image_id>-status-change',views.gallery_image_status_change,name='gallery_image_status_change'),
    path('gallery-edit-image-get',views.gallery_image_get,name='gallery_image_get'),
    path('gallery-image-edit',views.gallery_image_edit,name='gallery_image_edit'),
    path('gallery-image-<int:image_id>-delete',views.gallery_image_delete,name='gallery_image_delete')

]

urlpatterns +=[
    path('video-gallery-list',views.video_gallery_list,name='video_gallery_list'),
    path('video-add-gallery-list',views.video_add,name='video_add'),
    path('gallery-video-get',views.gallery_video_get,name='gallery_video_get'),
    path('gallery-video-update',views.video_update_save,name='video_update_save')
]