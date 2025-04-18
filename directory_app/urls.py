from django.urls import path
from . import views

urlpatterns = [ 
    # path('user/login/', views.userLogin, name="userLogin"), 
    path('', views.redirect_to_dashboard, name="redirect_to_dashboard"), 
    path('adminlogin/', views.dashboardLogin, name="dashboard_login"), 
    path('adminlogout/', views.dashboardLogout, name="dashboardLogout"), 
    path('dashboard/', views.dashboard_homepage, name="dashboard"),  
    
    path('persons/', views.person_list, name='person_list'),
    path('persons/add/', views.person_add, name='person_add'),
    path('persons/edit/<int:id>/', views.person_edit, name='person_edit'),
    path('persons/delete/<int:id>/', views.person_delete, name='person_delete'),
    path('person/details/<int:person_id>/', views.person_details, name='person_details'),

    # Company URLs
    path('company/', views.company_list, name='company_list'),
    path('company/add/', views.company_add, name='company_add'),
    # path('organization/edit/<int:id>/', views.organization_edit, name='organization_edit'),
    # path('organization/delete/<int:id>/', views.organization_delete, name='organization_delete'),
    # path('organization/details/<int:id>/', views.organization_delete, name='organization_details'),


    # Organization URLs
    path('organization/', views.organization_list, name='organization_list'),
    path('organization/add/', views.organization_add, name='organization_add'),
    path('organization/edit/<int:id>/', views.organization_edit, name='organization_edit'),
    path('organization/delete/<int:id>/', views.organization_delete, name='organization_delete'),
    path('organization/details/<int:id>/', views.organization_detail, name='organization_details'), 

    # SMS Module  
    path('send-sms/<int:person_id>/', views.send_single_sms, name='send_single_sms'),
    path('send-bulk-sms/', views.send_bulk_sms, name='send_bulk_sms'),
    path('create-sms-template/', views.create_sms_template, name='create_sms_template'),
    path('sent-sms-list/', views.send_sms_list, name='send_sms_list'),
    path('send-sms/', views.send_sms, name='send_sms'),

    ######### User list
    path('users/myprofile/', views.MyProfile, name='my_profile_details'),
    path('users/edit-profile/', views.EditProfile, name='edit_profile'),
    path('users/change-password/', views.ChangePassword, name='change_password'),

    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_create, name='user_add'),
    path('users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),


]

