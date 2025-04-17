from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.organizationAdd, name='organizationAdd'), 
    path('division/add/', views.division_add, name='division_add'),
    path('division/list/', views.division_list, name='division_list'),
    path('division/edit/<int:id>/', views.division_edit, name='division_edit'),
    path('division/delete/<int:id>/', views.division_delete, name='division_delete'),

    path('political-identity/add/', views.political_identity_add, name='political_identity_add'),
    path('political-identity/list/', views.political_identity_list, name='political_identity_list'),
    path('political-identity/edit/<int:id>/', views.political_identity_edit, name='political_identity_edit'),
    path('political-identity/delete/<int:id>/', views.political_identity_delete, name='political_identity_delete'),

    path('organization-category/add/', views.organization_category_add, name='organization_category_add'),
    path('organization-category/list/', views.organization_category_list, name='organization_category_list'),
    path('organization-category/edit/<int:id>/', views.organization_category_edit, name='organization_category_edit'),
    path('organization-category/delete/<int:id>/', views.organization_category_delete, name='organization_category_delete'),

    
    # Designation URLs
    path('designation/', views.designation_list, name='designation_list'),
    path('designation/add/', views.designation_add, name='designation_add'),
    path('designation/edit/<int:pk>/', views.designation_edit, name='designation_edit'),
    path('designation/delete/<int:pk>/', views.designation_delete, name='designation_delete'),


    
    # Person Level URLs
    path('personlevel/', views.personlevel_list, name='personlevel_list'),
    path('personlevel/add/', views.personlevel_add, name='personlevel_add'),
    path('personlevel/edit/<int:pk>/', views.personlevel_edit, name='personlevel_edit'),
    path('personlevel/delete/<int:pk>/', views.personlevel_delete, name='personlevel_delete'),




]
 
   