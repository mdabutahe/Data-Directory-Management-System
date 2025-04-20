from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from directory_app.models import *
from django.conf import settings
from django.http import JsonResponse
import requests
import json
from datetime import datetime
from directory_app.decorators import UserLogin
from directory_app.tasks import send_delayed_email


def redirect_to_dashboard(request):
    return redirect('/dashboard/')

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


def dashboardLogout(request):  
    request.session['user_id'] = False
    request.session['user_email'] = False
    request.session['first_name'] = False
    return redirect('/adminlogin/')




import pandas as pd
from django.core.mail import EmailMessage
import os
 
@UserLogin
def dashboard_homepage(request):
     
    # Local Excel file path on your Windows machine
    # excel_path = r'C:\Users\wempro\Downloads\interview_candidates.xlsx'
    excel_path = r'C:\Users\wempro\Downloads\InterviewCandidate_React.xlsx'

    # Sheet/tab name to read
    sheet_name = 'react123'

    # Read specific sheet/tab from Excel
    df = pd.read_excel(excel_path, sheet_name=sheet_name, engine='openpyxl')

    # Loop through rows and send emails
    count = 0
    for _, row in df.iterrows():
        name = row.get('Name')
        email = row.get('Email')
        # schedule_time = row.get('Schedule Time')
 
        # # I need find AM/PM from schedule_time
        # if schedule_time:
        #     schedule_time = schedule_time.strftime("%I:%M %p")
        # else:
        #     schedule_time = "Not Available"

        # print("schedule_time: ", schedule_time)

    
        # schedule_date = row.get('Schedule Date')
        # if schedule_date: 
        #     schedule_date = schedule_date.strftime(" %d %B %Y")
        # else:
        #     schedule_date = "Not Available"

        # print("schedule_date: ", schedule_date)
        # meeting_url = row.get('Meeting url')
 
 
        subject = "Coding Assignment (1-Day Extension) for the Next Step - Software Engineer Position at Wempro.com"

        message = f"""
        <html>
        <body style="font-family:Calibri, sans-serif; font-size:15px; color:#000;">
            <p><strong>Dear  Candidate,</strong> </p>

            <p>
                Thank you for participating in the initial interview for the <strong>Software Engineer - ReactJS Developer</strong> position at Wempro. As part of the next step in the selection process, we would like you to complete a coding assignment to further assess your skills.
            </p>
            <p>
                Please follow the example JSON provided below. First, create a JSON object like the one shown and send it via a POST API call. After submitting, you will receive the same JSON in response. Use this JSON to rebuild the form builder dynamically.
                <br>
                If you update any field in the form, it should be updated by making another POST API call with the modified JSON.

                ...
                    <pre style="background:#f4f4f4; padding:10px; border-radius:6px; overflow:auto;">
                    <code>
                    [
                    {{
                        "fieldsetName": "Fieldset 1",
                        "fieldsetTextId": "fieldset1",
                        "fields": [
                        {{
                            "labelName": "first input",
                            "labelTextId": "firstinput",
                            "inputType": "text",
                            "options": ""
                        }},
                        {{
                            "labelName": "second input",
                            "labelTextId": "secondinput",
                            "inputType": "number",
                            "options": ""
                        }},
                        {{
                            "labelName": "third input",
                            "labelTextId": "thirdinput",
                            "inputType": "select",
                            "options": ["option1", "option2", "option3"]
                        }},
                        {{
                            "labelName": "fourth input",
                            "labelTextId": "fourthinput",
                            "inputType": "select",
                            "options": ["1", "2", "3", "4", "5"]
                        }}
                        ]
                    }},
                    {{
                        "fieldsetName": "Fieldset 2",
                        "fieldsetTextId": "fieldset2",
                        "fields": [
                        {{
                            "labelName": "first input",
                            "labelTextId": "firstinput",
                            "inputType": "text",
                            "options": ""
                        }},
                        {{
                            "labelName": "second input",
                            "labelTextId": "secondinput",
                            "inputType": "number",
                            "options": ""
                        }},
                        {{
                            "labelName": "third input",
                            "labelTextId": "thirdinput",
                            "inputType": "select",
                            "options": ["option1", "option2", "option3"]
                        }},
                        {{
                            "labelName": "fourth input",
                            "labelTextId": "fourthinput",
                            "inputType": "select",
                            "options": ["1", "2", "3", "4", "5"]
                        }}
                        ]
                    }}
                    ]
                    </code>
                    </pre>
                    ...


            </p>
           
            <p><strong>Important Links</strong> </p>

            <strong>API Link(GET and POST) :</strong> <a href="http://team.dev.helpabode.com:54292/api/wempro/react-dev/coding-test/{email}"> http://team.dev.helpabode.com:54292/api/wempro/react-dev/coding-test/{email}</a> <br><br>

            <strong>Assignment Link:</strong> <a href="https://docs.google.com/document/d/1EgClyqyLnZJvrnOI1lW-TOlNvEw9rCG8Gx564KEWrGU/edit?usp=sharing"> https://docs.google.com/document/d/1EgClyqyLnZJvrnOI1lW-TOlNvEw9rCG8Gx564KEWrGU/edit?usp=sharing</a>
            
            <p>
                <strong>Figma Link:</strong> (Password: dot-haze-happy-spline) <br>
                <a href="https://www.figma.com/design/4s1TgLkvConnhaiG9pzaxo/ReactJS-Coding-Assignment?node-id=0-1&t=3BQ86xzdKqEF9efT-1">https://www.figma.com/design/4s1TgLkvConnhaiG9pzaxo/ReactJS-Coding-Assignment?node-id=0-1&t=3BQ86xzdKqEF9efT-1</a><br>
            </p>

 
            <p><strong>Coding Assignment Deadline Extension:</strong></p> 
            <ul>
                <li><strong> Deadline: </strong> Sunday, 20th April 2025, 11:59 PM</li> 
            </ul>

            <p>
               Please review the details and submit the assignment within the given timeline. 
            </p>
            <p>
               We are excited to see your work and further evaluate your skills. 
            </p>
            <p>
              If you have any questions or need clarification on any part of the assignment, please don't hesitate to reach out.
            </p>
 

            <br> 
            <p> 
                Jane Alam Khan <br>
                Recruiter<br>
                Phone: 01717-876918<br>
                Email: <a href="mailto:jane.khan@wempro.com">jane.khan@wempro.com</a>
            </p>
            <img src="https://helpabode.com/img/wempro_logo.png" alt="Wempro">
        </body>
        </html>
        """
        cc_emils = ["nur.mohammad@wempro.com", "jane.khan@wempro.com", "faruk@wempro.com", "akkas.mia@wempro.com"]
        # cc_emils = ["akkas.mia@wempro.com"]
        
        sender_name = "Wempro Recruiter"
        sender_email = "wemproteams@gmail.com"

        # Construct the full "From" field with custom display name
        from_email = f"{sender_name} <{sender_email}>"
        
        if str(email) != "nan": 
            
            # mail = EmailMessage(subject, message, from_email, to=[email], cc=cc_emils)
            # mail.content_subtype = "html"  
            # mail.send()

            print("Email sent success to: ", email)
            count += 1
            print(count)
            
 

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
 
    return render(request, 'index.html', {
        'total_organizations': total_organizations,
        'total_persons': total_persons,
        'total_sms': total_sms,
        'data': data,  # Pass the division-wise data
        'months': months,  # Pass the month names for the chart
        'colors': colors  # Pass the division colors
    })
 
@UserLogin
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization/organization_list.html', {'organizations': organizations})

# Add Organization
@UserLogin
def organization_add(request):
    divisions = Division.objects.all()
    categories = OrganizationCategory.objects.all()

    if request.method == 'POST':
        division = Division.objects.get(id=request.POST['division'])
        category = OrganizationCategory.objects.get(id=request.POST['category'])
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        mobile1 = request.POST.get('mobile1', '')
        mobile2 = request.POST.get('mobile2', '')
        address = request.POST.get('address', '')
        website = request.POST.get('website', '')
        map_location = request.POST.get('map_location', '')

        Organization.objects.create(
            division=division,
            category=category,
            name=name,
            email=email,
            phone=phone,
            mobile1=mobile1,
            mobile2=mobile2,
            address=address,
            website=website,
            map_location=map_location
        )
        return redirect('organization_list')

    return render(request, 'organization/organization_add.html', {'divisions': divisions, 'categories': categories})

# Edit Organization
def organization_edit(request, id):
    organization = get_object_or_404(Organization, id=id)
    divisions = Division.objects.all()
    categories = OrganizationCategory.objects.all()

    if request.method == 'POST':
        organization.division = Division.objects.get(id=request.POST['division'])
        organization.category = OrganizationCategory.objects.get(id=request.POST['category'])
        organization.name = request.POST['name']
        organization.email = request.POST['email']
        organization.phone = request.POST.get('phone', '')
        organization.mobile1 = request.POST.get('mobile1', '')
        organization.mobile2 = request.POST.get('mobile2', '')
        organization.address = request.POST.get('address', '')
        organization.website = request.POST.get('website', '')
        organization.map_location = request.POST.get('map_location', '')

        organization.save()
        return redirect('organization_list')

    return render(request, 'organization/organization_edit.html', {'organization': organization, 'divisions': divisions, 'categories': categories})

# Delete Organization
def organization_delete(request, id):
    organization = get_object_or_404(Organization, id=id)

    if organization:
        organization.delete()
        return redirect('organization_list')
 




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
        organization_id = request.POST.get("organization")
        designation_id = request.POST.get("designation")
        person_level_id = request.POST.get("person_level")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        mobile = request.POST.get("mobile")
        whatsapp = request.POST.get("whatsapp")
        address = request.POST.get("address")
        rank = request.POST.get("rank", 1)
        profile_details = request.POST.get("profile_details")

        try:
            organization = Organization.objects.get(id=organization_id)
            designation = Designation.objects.get(id=designation_id)
            person_level = PersonLevel.objects.get(id=person_level_id)

            person = PersonList.objects.create(
                organization=organization,
                designation=designation,
                person_level=person_level,
                name=name,
                email=email,
                phone=phone,
                mobile=mobile,
                whatsapp=whatsapp,
                address=address,
                rank=rank,
                profile_details=profile_details,
            )
            person.save()
            messages.success(request, "Person added successfully!")
            return redirect("person_list")  # Redirect to the list page

        except Organization.DoesNotExist:
            messages.error(request, "Invalid Organization selected.")
        except Designation.DoesNotExist:
            messages.error(request, "Invalid Designation selected.")
        except PersonLevel.DoesNotExist:
            messages.error(request, "Invalid Person Level selected.")

    organizations = Organization.objects.all()
    designations = Designation.objects.all()
    person_levels = PersonLevel.objects.all()

    return render(request, "member/person_add.html", {
        "organizations": organizations,
        "designations": designations,
        "person_levels": person_levels,
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
 

 

# List All Sent Emails
def email_list(request):
    emails = BulkEmail.objects.all().order_by("-sent_date")
    return render(request, "email/email_list.html", {"emails": emails})

# Send a Single Email
def send_email(request, person_id):
    person = get_object_or_404(PersonList, id=person_id)

    if request.method == "POST":
        email = person.email
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Store email in database (Default: Failed)
        email_entry = BulkEmail.objects.create(
            person=person,
            subject=subject,
            message=message,
            status="Failed",  # Default status
        )

        send_delayed_email.delay(email, subject, message)

        print("Email sent to:", email)

        ### using fultiple email sending method
        # send_delayed_email.apply_async(
        #     args=['user@example.com', 'Welcome!', 'Thanks for joining!'],
        #     countdown=60  # delay by 1 minute
        # )
                

        # # Send Email Logic
        # try:
        #     send_mail(
        #         subject,
        #         message,
        #         'wemproteams@gmail.com',  # Sender email
        #         [person.email],  # Recipient email
        #         fail_silently=False,
        #     )
        #     email_entry.status = "Sent"
        #     email_entry.save()
        #     messages.success(request, "Email sent successfully.")
        # except Exception as e:
        #     messages.error(request, f"Failed to send email: {e}")

        return redirect("email_list")

    return render(request, "email/send_email.html", {"person": person})

#  Edit an Email (Only Subject & Message)
def edit_email(request, email_id):
    email_entry = get_object_or_404(BulkEmail, id=email_id)

    if request.method == "POST":
        email_entry.subject = request.POST.get("subject")
        email_entry.message = request.POST.get("message")
        email_entry.save()
        messages.success(request, "Email updated successfully.")
        return redirect("email_list")

    return render(request, "email/edit_email.html", {"email": email_entry})

#   Delete an Email
def delete_email(request, email_id):
    email_entry = get_object_or_404(BulkEmail, id=email_id)
    email_entry.delete()
    messages.success(request, "Email deleted successfully.")
    return redirect("email_list")



import uuid

# Generate random text_id
def generate_text_id():
    return str(uuid.uuid4())[:8]  # Generates an 8-character unique ID

# List View
def follow_up_list(request):
    followups = OrganizationFollowUp.objects.all()
    return render(request, 'followup/follow_up_list.html', {'followups': followups})

# Create View
def follow_up_create(request):
    print(request.user)
    if request.method == "POST":
        text_id = generate_text_id()
        organization_id = request.POST.get('organization')
        person_id = request.POST.get('person')
        mobile = request.POST.get('mobile')
        next_follow_up_date = request.POST.get('next_follow_up_date')
        status = request.POST.get('status')
        follow_up_for = request.POST.get('follow_up_for')
        feedback = request.POST.get('feedback')
        follow_up_by = request.user  # Assuming logged-in user

        organization = get_object_or_404(Organization, pk=organization_id)
        person = get_object_or_404(PersonList, pk=person_id)

        followup = OrganizationFollowUp.objects.create(
            text_id=text_id,
            organization=organization,
            person=person,
            mobile=mobile,
            next_follow_up_date=next_follow_up_date,
            status=status,
            follow_up_for=follow_up_for,
            feedback=feedback,
            follow_up_by=follow_up_by
        )

        messages.success(request, "Follow-up created successfully!")
        return redirect('follow_up_list')

    organizations = Organization.objects.all()
    persons = PersonList.objects.all()
    return render(request, 'followup/follow_up_form.html', {'organizations': organizations, 'persons': persons})

# Update View
def follow_up_update(request, pk):
    followup = get_object_or_404(OrganizationFollowUp, pk=pk)
    
    if request.method == "POST":
        followup.organization = get_object_or_404(Organization, pk=request.POST.get('organization'))
        followup.person = get_object_or_404(PersonList, pk=request.POST.get('person'))
        followup.mobile = request.POST.get('mobile')
        followup.next_follow_up_date = request.POST.get('next_follow_up_date')
        followup.status = request.POST.get('status')
        followup.follow_up_for = request.POST.get('follow_up_for')
        followup.feedback = request.POST.get('feedback')
        followup.save()
        
        messages.success(request, "Follow-up updated successfully!")
        return redirect('follow_up_list')

    organizations = Organization.objects.all()
    persons = PersonList.objects.all()
    return render(request, 'followup/follow_up_form.html', {'followup': followup, 'organizations': organizations, 'persons': persons})

# Delete View
def follow_up_delete(request, pk):
    followup = get_object_or_404(OrganizationFollowUp, pk=pk)
    if request.method == "POST":
        followup.delete()
        messages.success(request, "Follow-up deleted successfully!")
        return redirect('follow_up_list')
    
    return render(request, 'followup/follow_up_confirm_delete.html', {'followup': followup})






# import pandas as pd
# from django.core.mail import EmailMessage
# import os
 
# def BulkEmailFromAdmin(request):
#     try:
#         # Local Excel file path on your Windows machine
#         excel_path = r'C:\Users\wempro\Downloads\interview_candidates.xlsx'

#         # Sheet/tab name to read
#         sheet_name = 'React Js'

#         # Read specific sheet/tab from Excel
#         df = pd.read_excel(excel_path, sheet_name=sheet_name, engine='openpyxl')

#         # Loop through rows and send emails
#         for _, row in df.iterrows():
#             name = row.get('Name')
#             email = row.get('Email')
#             schedule_time = row.get('Schedule Time')
#             meeting_url = row.get('Meeting url')

#             subject = "Interview Invitation - React Developer Role"
#             message = (
#                 f"Dear {name},\n\n"
#                 f"You have been shortlisted for an interview. Please find the details below:\n\n"
#                 f"🗓 Schedule Time: {schedule_time}\n"
#                 f"📍 Meeting Link: {meeting_url}\n\n"
#                 f"Best of luck!\nTeam HR"
#             )

#             mail = EmailMessage(subject, message, to=[email])
#             mail.send()

#         return Response({"message": "Emails sent successfully."}, status=status.HTTP_200_OK)

#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

 
@UserLogin
def association_list(request):
    name_query = request.GET.get('name', '')
    email_query = request.GET.get('email', '')
    phone_query = request.GET.get('phone', '')

    associations = Association.objects.all()

    if name_query:
        associations = associations.filter(name__icontains=name_query)
    if email_query:
        associations = associations.filter(email__icontains=email_query)
    if phone_query:
        associations = associations.filter(phone__icontains=phone_query)

    context = {
        'associations': associations,
        'name_query': name_query,
        'email_query': email_query,
        'phone_query': phone_query,
    }
    return render(request, 'association/association_list.html', context)


@UserLogin
def association_add(request):
    divisions = Division.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        established_date = request.POST.get('established_date')
        division_id = request.POST.get('division')

        division = Division.objects.get(id=division_id) if division_id else None

        Association.objects.create(
            name=name,
            address=address,
            phone=phone,
            email=email,
            established_date=established_date,
            division=division
        )

        messages.success(request, 'Association added successfully.')
        return redirect('association_list')

    return render(request, 'association/association_add.html', {'divisions': divisions})

@UserLogin
def association_edit(request, pk):
    association = get_object_or_404(Association, pk=pk)
    divisions = Division.objects.all()

    if request.method == 'POST':
        association.name = request.POST.get('name')
        association.address = request.POST.get('address')
        association.phone = request.POST.get('phone')
        association.email = request.POST.get('email')
        association.established_date = request.POST.get('established_date')
        division_id = request.POST.get('division')

        association.division = Division.objects.get(id=division_id) if division_id else None

        association.save()
        messages.success(request, 'Association updated successfully.')
        return redirect('association_list')

    return render(request, 'association/association_edit.html', {
        'association': association,
        'divisions': divisions
    })

@UserLogin
def association_delete(request, pk):
    association = get_object_or_404(Association, pk=pk)
    association.delete()
    messages.success(request, 'Association deleted successfully.')
    return redirect('association_list')





