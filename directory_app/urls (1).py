from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.redirect_to_dashboard, name="redirect_to_dashboard"), 
    path('adminlogin/', views.dashboardLogin, name="dashboard_login"), 
    path('adminlogout/', views.dashboardLogout, name="dashboardLogout"), 
    path('dashboard/', views.dashboard_homepage, name="dashboard"),  
    
    path('persons/', views.person_list, name='person_list'),
    path('persons/add/', views.person_add, name='person_add'),
    path('persons/edit/<int:id>/', views.person_edit, name='person_edit'),
    path('persons/delete/<int:id>/', views.person_delete, name='person_delete'),
    path('person/details/<int:person_id>/', views.person_details, name='person_details'),

    # Organization URLs
    path('organization/', views.organization_list, name='organization_list'),
    path('organization/add/', views.organization_add, name='organization_add'),
    path('organization/edit/<int:id>/', views.organization_edit, name='organization_edit'),
    path('organization/delete/<int:id>/', views.organization_delete, name='organization_delete'),
    path('organization/details/<int:id>/', views.organization_delete, name='organization_details'),


    # SMS Module  
    path('send-sms/<int:person_id>/', views.send_single_sms, name='send_single_sms'),
    path('send-bulk-sms/', views.send_bulk_sms, name='send_bulk_sms'),
    path('sent-sms-list/', views.send_sms_list, name='send_sms_list'),

    # Email Send Module 
    path("send-email/<int:person_id>/", views.send_email, name="send_single_email"),
    path("email-list/", views.email_list, name="email_list"),
    path("edit-email/<int:email_id>/", views.edit_email, name="edit_email"),
    path("delete-email/<int:email_id>/", views.delete_email, name="delete_email"),

    ######### User list
    path('users/myprofile/', views.MyProfile, name='my_profile_details'),
    path('users/edit-profile/', views.EditProfile, name='edit_profile'),
    path('users/change-password/', views.ChangePassword, name='change_password'),

    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_create, name='user_add'),
    path('users/edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:user_id>/', views.user_delete, name='user_delete'),


    path('followups/', views.follow_up_list, name='follow_up_list'),
    path('followups/create/', views.follow_up_create, name='follow_up_create'),
    path('followups/update/<int:pk>/', views.follow_up_update, name='follow_up_update'),
    path('followups/delete/<int:pk>/', views.follow_up_delete, name='follow_up_delete'),


    path('association/', views.association_list, name='association_list'),
    path('association/add/', views.association_add, name='association_add'),
    path('association/edit/<int:pk>/', views.association_edit, name='association_edit'),
    path('association/delete/<int:pk>/', views.association_delete, name='association_delete'),

 

]
 
 