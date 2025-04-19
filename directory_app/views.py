from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from directory_app.models import *
from django.conf import settings
from django.http import JsonResponse
import requests
import json
from datetime import datetime
from directory_app.decorators import UserLogin
 

def dashboardLogin(request):
    if request.session.get('user_id'):
        return redirect('/dashboard/')
 
    if request.method == "POST":
        get_data = UserList.objects.filter(email = request.POST['email'], password = request.POST['password']).first()
        if get_data:
            request.session['user_id'] = get_data.id 
            request.session['user_email'] = get_data.email
            request.session['first_name'] = get_data.first_name 
            request.session['user_image'] = str(get_data.image) if get_data.image  else None
            return redirect('/dashboard/')
        else:
            return redirect('/adminlogin/') 

 
    return render(request, "login.html")


def redirect_to_dashboard(request):
    return redirect('/dashboard/')


def dashboardLogout(request):  
    request.session['user_id'] = False
    request.session['user_email'] = False
    request.session['first_name'] = False
    return redirect('/adminlogin/')


@UserLogin
def dashboard_homepage(request):
    # Get total counts
    total_organizations = Organization.objects.count()
    total_persons = PersonList.objects.count()
    total_sms = SentSMSList.objects.count()

    # Get the current month and year
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    
    # Generate month names dynamically (January to current month)
    months = [datetime(current_year, month, 1).strftime('%B') for month in range(1, current_month + 1)]
    
    # Fetch all unique divisions from the Division model
    divisions = Division.objects.all()

    data = {}
    colors = {}

    # Calculate monthly person counts per division and get color for each division
    for division in divisions:
        monthly_counts = []
        for month in range(1, current_month + 1):
            count = PersonList.objects.filter(
                organization__division=division,
                created__year=current_year,
                created__month=month
            ).count()
            monthly_counts.append(count)
        data[division.name] = monthly_counts
        colors[division.name] = division.color  # Store the division color

    print(data)
    print(months)
    print(colors)
    return render(request, 'index.html', {
        'total_organizations': total_organizations,
        'total_persons': total_persons,
        'total_sms': total_sms,
        'data': data,  # Pass the division-wise data
        'months': months,  # Pass the month names for the chart
        'colors': colors  # Pass the division colors
    })
 
def organization_list(request):
    divisions = Division.objects.all()
    organizations = Organization.objects.all()
    return render(request, 'organization/organization_list.html', {'organizations': organizations, 'divisions': divisions})

# Add Organization
def organization_add(request):
    divisions = Division.objects.all()
    designations = Designation.objects.all().order_by('rank')
    categories = OrganizationCategory.objects.all()

    if request.method == 'POST':
        division_id = request.POST['division']
        company_name = request.POST['company_name']
        category_id = int(request.POST['company_category']) 
        mobile1 = request.POST.get('mobile1')
        mobile2 = request.POST.get('mobile2')
        mobile3 = request.POST.get('mobile3')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email3 = request.POST.get('email3') 
        website = request.POST.get('website')
        social_facebook = request.POST.get('social_facebook')
        social_linkedin = request.POST.get('social_linkedin')
        office_address = request.POST.get('office_address')
        residential_address = request.POST.get('residential_address')
        notes = request.POST.get('notes')

        Organization.objects.create( 
            division_id=division_id,
            category_id=category_id, 
            org_name=company_name, 
            email1=email1,
            email2=email2,
            email3=email3, 
            mobile1=mobile1,
            mobile2=mobile2,
            mobile3=mobile3, 
            website=website,social_facebook = social_facebook,social_linkedin=social_linkedin,
            office_address=office_address, residential_address = residential_address, notes= notes,
        )
        return redirect('organization_list')
    context = {
        'divisions': divisions, 
        'designations': designations,
        'categories': categories,
    }
    return render(request, 'organization/organization_add.html', context)

# Edit Organization
def organization_edit(request, id):
    organization = get_object_or_404(Organization, id=id)
    
    divisions = Division.objects.all() 
    categories = OrganizationCategory.objects.all()

    if request.method == 'POST':
        organization.division = Division.objects.get(id=request.POST['division'])
        organization.category = OrganizationCategory.objects.get(id=request.POST['company_category']) 
        organization.org_name = request.POST['org_name'] 
        organization.email1 = request.POST['email1']
        organization.email2 = request.POST['email2']
        organization.email3 = request.POST['email3'] 
        organization.mobile1 = request.POST.get('mobile1', '')
        organization.mobile2 = request.POST.get('mobile2', '')
        organization.mobile3 = request.POST.get('mobile3', '')
        organization.social_facebook = request.POST.get('social_facebook')
        organization.social_linkedin = request.POST.get('social_linkedin')
        organization.office_address = request.POST.get('office_address')
        organization.residential_address = request.POST.get('residential_address')
        organization.website = request.POST.get('website')
        organization.notes = request.POST.get('notes')

        organization.save()
        return redirect('organization_list')

    context = { 
        "categories": categories,
        "organization": organization,
        "divisions": divisions,
    }
    return render(request, 'organization/organization_edit.html', context)

# Delete Organization
def organization_delete(request, id):
    organization = get_object_or_404(Organization, id=id)

    if organization:
        organization.delete()
        return redirect('organization_list')
 

def organization_detail(request, id):
    organization = get_object_or_404(Organization, id=id)
    return render(request, 'organization/organization_details.html', {'organization': organization})




def person_list(request):
    persons = PersonList.objects.all().order_by('-id')

    # Get filter values from GET request
    division_id = request.GET.get('division')
    organization_id = request.GET.get('organization')
    person_level_id = request.GET.get('person_level')
    designation_id = request.GET.get('designation')
    mobile = request.GET.get('mobile')
    email = request.GET.get('email')

    # Apply filters
    if division_id:
        persons = persons.filter(organization__division_id=division_id)
    if organization_id:
        persons = persons.filter(organization_id=organization_id)
    if person_level_id:
        persons = persons.filter(person_level_id=person_level_id)
    if designation_id:
        persons = persons.filter(designation_id=designation_id)
    if mobile:
        persons = persons.filter(phone__icontains=mobile)
    if email:
        persons = persons.filter(email__icontains=email)

    # Fetch data for dropdown filters
    divisions = Division.objects.all()
    organizations = Organization.objects.all()
    designations = Designation.objects.all()
    person_levels = PersonLevel.objects.all()

    return render(request, 'member/person_list.html', {
        'persons': persons,
        'divisions': divisions,
        'organizations': organizations,
        'designations': designations,
        'person_levels': person_levels,
    })




def person_add(request):
    if request.method == "POST":
        company_id = request.POST.get("company_id")
        organization_id = request.POST.get("organization")
        designation_id = request.POST.get("designation")
        person_level_id = request.POST.get("person_level")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        mobile = request.POST.get("mobile")
        whatsapp = request.POST.get("whatsapp")
        twitter_link = request.POST.get("twitter_link")
        linkedin_link = request.POST.get("linkedin_link")
        facebook_link = request.POST.get("facebook_link")
        address = request.POST.get("address") 
        profile_details = request.POST.get("profile_details")
        political_identity_id = request.POST.get("political_identity")

        try:
            company = CompanyList.objects.get(id=company_id) if company_id else None
            organization = Organization.objects.get(id=organization_id) if organization_id else None
            designation = Designation.objects.get(id=designation_id) if designation_id else None
            person_level = PersonLevel.objects.get(id=person_level_id) if person_level_id else None
            political_identity = PoliticalIdentity.objects.get(id=political_identity_id) if political_identity_id else None

            person = PersonList.objects.create(
                company=company, organization=organization,
                designation=designation,
                person_level=person_level,
                name=name, email=email, phone=phone, 
                twitter_link = twitter_link, linkedin_link = linkedin_link,
                 facebook_link = facebook_link,
                mobile=mobile, political_identity = political_identity,
                whatsapp=whatsapp,
                address=address, 
                profile_details=profile_details,
            )
            person.save()
            messages.success(request, "Person added successfully!")
            return redirect("person_list") 

        except Organization.DoesNotExist:
            messages.error(request, "Invalid Organization selected.")
        except Designation.DoesNotExist:
            messages.error(request, "Invalid Designation selected.")
        except PersonLevel.DoesNotExist:
            messages.error(request, "Invalid Person Level selected.")

    company_list = CompanyList.objects.all()
    organizations = Organization.objects.all()
    designations = Designation.objects.all()
    person_levels = PersonLevel.objects.all()
    political_list = PoliticalIdentity.objects.all()

    return render(request, "member/person_add.html", {
        "company_list": company_list,
        "organizations": organizations,
        "designations": designations,
        "person_levels": person_levels,
        "political_list": political_list,
    })


def person_edit(request, id):
    person = get_object_or_404(PersonList, id=id)
    organizations = Organization.objects.all()
    person_levels = PersonLevel.objects.all()
    designations = Designation.objects.all()

    if request.method == "POST":
        person.name = request.POST.get("name")
        person.email = request.POST.get("email")
        person.phone = request.POST.get("phone")
        person.whatsapp = request.POST.get("whatsapp")
        person.organization_id = request.POST.get("organization")
        person.person_level_id = request.POST.get("person_level")
        person.designation_id = request.POST.get("designation")
        person.location = request.POST.get("location")
        person.website = request.POST.get("website")
        person.other_links = request.POST.get("other_links")
        person.profile_details = request.POST.get("profile_details")
        person.address = request.POST.get("address")
        person.rank = request.POST.get("rank")

        person.save()
        return redirect("person_list")  # Redirect to person list after updating

    context = {
        "person": person,
        "organizations": organizations,
        "person_levels": person_levels,
        "designations": designations,
    }
    return render(request, "member/person_edit.html", context)

def person_delete(request, id):
    person = get_object_or_404(PersonList, id=id)
    person.delete()
    return redirect('person_list')



def person_details(request, person_id):
    person = get_object_or_404(PersonList, id=person_id)
    return render(request, 'member/person_details.html', {'person': person})


 



######################## SMS Module ###############################

 
# Function to simulate SMS sending (WITHOUT API - Active)
def send_sms_without_api(phone, message):
    print(f"SIMULATED: Sending SMS to {phone}: {message}")  # Debugging
    if phone:  # Simulated success/failure
        return "Success"
    return "Failed"

# Function to send SMS using an API (Commented Out)
# def send_sms_with_api(phone, message):
#     API_KEY = "your_api_key_here"  # Replace with actual API key
#     API_URL = "https://sms-api.com/send"  # Replace with actual API URL
#     payload = {
#         "api_key": API_KEY,
#         "to": phone,
#         "message": message
#     }
#     try:
#         response = requests.post(API_URL, json=payload)
#         if response.status_code == 200:
#             return "Success"
#         else:
#             return "Failed"
#     except Exception as e:
#         print(f"SMS API Error: {e}")
#         return "Failed"

# Send single SMS function
def send_single_sms(request, person_id):
    person = get_object_or_404(PersonList, id=person_id)

    if request.method == "POST":
        message = request.POST.get('message')

        # Store in database as Pending
        sms_record = SentSMSList.objects.create(person=person, phone=person.mobile, message=message, status='Pending')

        # Send SMS (Without API)
        sms_status = send_sms_without_api(person.mobile, message)

        # Update status in database
        sms_record.status = sms_status
        sms_record.save()

        messages.success(request, f"SMS {'sent' if sms_status == 'Success' else 'failed'} to {person.name}!")
        return redirect('send_sms_list')

    return render(request, 'sms/send_single_sms.html', {'person': person})

# Send bulk SMS function
def send_bulk_sms(request):
    if request.method == "POST":
        selected_persons = request.POST.getlist('selected_persons')
        message = request.POST.get('message')

        if not selected_persons or not message:
            messages.error(request, "Please select at least one person and enter a message.")
            return redirect('send_bulk_sms')

        recipients = PersonList.objects.filter(id__in=selected_persons)

        for person in recipients:
            sms_record = SentSMSList.objects.create(
                person=person,
                phone=person.mobile,
                message=message,
                status="Pending"
            )
            sms_status = send_sms_without_api(person.mobile, message)

            # Update status in database
            sms_record.status = sms_status
            sms_record.save()

            # Uncomment when you get an API key
            # response = send_sms_api(person.phone, message)
            # if response['status'] == "success":
            #     BulkSMS.objects.filter(person=person).update(status="Sent")
            # else:
            #     BulkSMS.objects.filter(person=person).update(status="Failed")

        messages.success(request, "Bulk SMS stored successfully. Will send when API is available.")
        return redirect('send_bulk_sms')

    persons = PersonList.objects.all()
    return render(request, 'sms/send_bulk_sms.html', {'persons': persons})



# Sent SMS list function
def send_sms_list(request):
    sent_sms = SentSMSList.objects.all().order_by('-created')
    return render(request, 'sms/send_sms_list.html', {'sent_sms': sent_sms})

# Create SMS template function
def create_sms_template(request):
    return render(request, "sms/create_sms_template.html")
# Create SMS template function
def send_sms(request):
    return render(request, "sms/send_single_sms.html")



# Company URLs
def company_list(request):
    companies = CompanyList.objects.all().order_by('-id')
    return render(request, 'company/company_list.html', {"companies": companies})
# Company URLs
def company_add(request): 
    categories = OrganizationCategory.objects.all()
 
    if request.method == 'POST': 
        company_name = request.POST['company_name']
        category_id = int(request.POST['company_category']) 
        mobile1 = request.POST.get('phone1')
        mobile2 = request.POST.get('phone2')
        mobile3 = request.POST.get('phone3')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email3 = request.POST.get('email3') 
        website = request.POST.get('website')
        social_facebook = request.POST.get('social_facebook')
        social_linkedin = request.POST.get('social_linkedin')
        office_address = request.POST.get('office_address')
        residential_address = request.POST.get('residential_address')
        about_company = request.POST.get('about_company')

        CompanyList.objects.create(  
            category_id=category_id, 
            company_name=company_name, 
            email1=email1, email2=email2, email3=email3, 
            mobile1=mobile1, mobile2=mobile2, mobile3=mobile3, 
            website=website,social_facebook = social_facebook,social_linkedin=social_linkedin,
            office_address=office_address, residential_address = residential_address, 
            about_company= about_company
        )
        return redirect('company_list')
    
    context = { 
        'categories':categories,
    }
    return render(request, 'company/company_add.html', context)




###################### List Users #####################
@UserLogin
def MyProfile(request):

    user_id = request.session.get('user_id')  
    user = UserList.objects.get(id=user_id)   
 
    return render(request, 'users/my_profile.html', {'user': user})



@UserLogin
def EditProfile(request):
    user_id = request.session.get('user_id')
    user = UserList.objects.get(id=user_id)

    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")

        if "image" in request.FILES:
            user.image = request.FILES["image"]

        user.save()
        request.session['user_image'] = str(user.image)
        messages.success(request, "Profile updated successfully.")
        
        return redirect("/users/myprofile/")

    return render(request, "users/edit_profile.html", {"user": user})


@UserLogin
def ChangePassword(request):
    user_id = request.session.get('user_id')
    user = UserList.objects.get(id=user_id)

    if request.method == "POST":
        
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if user.password != current_password:
            messages.warning(request, "Current Password Not Match.")
            return render(request, "users/change_password.html")


        if new_password == confirm_password: 
            user.password = new_password
            user.save()
            messages.success(request, "Password updated successfully.")
            return redirect("/users/myprofile/")
        
        else:
            messages.warning(request, "Password Not Match.")
            return render(request, "users/change_password.html")
 
    return render(request, "users/change_password.html")



def user_list(request):
    users = UserList.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# Create User
def user_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name', '')
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        user_id = request.POST.get('user_id', '')
        password = request.POST['password']
        status = request.POST.get('status', 'off') == 'on'
        
        image = request.FILES.get('image')  # Handle image upload

        UserList.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            user_id=user_id,
            password=password,
            image=image,
            status=status
        )
        messages.success(request, "User created successfully!")
        return redirect('user_list')

    return render(request, 'users/user_form.html', {'action': 'Add'})

# Edit User
def user_edit(request, user_id):
    user = get_object_or_404(UserList, id=user_id)

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST['email']
        user.phone = request.POST.get('phone', '')
        user.user_id = request.POST.get('user_id', '')
        user.password = request.POST['password'] 
        user.address = request.POST['address'] 
        user.status = request.POST.get('status', 'off') == 'on'

        if 'image' in request.FILES:
            user.image = request.FILES['image']  # Handle image upload

        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('user_list')

    return render(request, 'users/user_form.html', {'user': user, 'action': 'Edit'})

# Delete User
def user_delete(request, user_id):
    user = get_object_or_404(UserList, id=user_id) 
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('user_list')
 


