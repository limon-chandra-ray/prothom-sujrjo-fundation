from django.urls import path
from . import views
app_name = 'sadmin'
urlpatterns = [
    path('',views.dashboard,name='dashboard')
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
    path('slide-get',views.get_slide,name='get_slide')
]


# sponsor urls section
urlpatterns +=[
    path('sponsor-list',views.child_sponsor_list_view,name='child_sponsor_list_view')
]

# authentication system section
urlpatterns +=[
    path('log-in',views.login_view,name='login_view')
]