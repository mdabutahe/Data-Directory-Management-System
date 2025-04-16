from django.db import models
 

# Division Model
class Division(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rank = models.IntegerField(default=1)
    color = models.CharField(max_length=50, default="green")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'division'
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        return self.name


# Political Identity Model
class PoliticalIdentity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rank = models.IntegerField(default=1) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'political_identity'
        verbose_name = 'PoliticalIdentity'
        verbose_name_plural = 'PoliticalIdentitys'

    def __str__(self):
        return self.name


# OrganizationCategory Model
class OrganizationCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rank = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization_category'
        verbose_name = 'Organization Category'
        verbose_name_plural = 'Organization Categories'

    def __str__(self):
        return self.name


# Designation Model
class Designation(models.Model):
    name = models.CharField(max_length=255)
    rank = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'designation'
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        return self.name


# PersonLevel Model
class PersonLevel(models.Model):
    name = models.CharField(max_length=255)
    rank = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'person_level'
        verbose_name = 'Person Level'
        verbose_name_plural = 'Person Levels'

    def __str__(self):
        return self.name


# PersonList Model
class PersonList(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    person_level = models.ForeignKey('PersonLevel', on_delete=models.CASCADE)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)  
    profile_details = models.TextField(blank=True, null=True)
    rank = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'person_list'
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.name


# PersonFollowUp Model
class PersonFollowUp(models.Model):
    person = models.ForeignKey('PersonList', on_delete=models.CASCADE)
    follow_up_date = models.DateTimeField()
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'person_follow_up'
        verbose_name = 'Person Follow-Up'
        verbose_name_plural = 'Person Follow-Ups'

    def __str__(self):
        return f"Follow-up for {self.person.name} on {self.follow_up_date}"


# Marketing Activity Model
class MarketingActivity(models.Model):
    person = models.ForeignKey('PersonList', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=[('Email', 'Email'), ('SMS', 'SMS'), ('Social Media', 'Social Media'), ('Call', 'Call')])
    activity_details = models.TextField()
    activity_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marketing_activity'
        verbose_name = 'Marketing Activity'
        verbose_name_plural = 'Marketing Activities'

    def __str__(self):
        return f"{self.activity_type} for {self.person.name} on {self.activity_date}"


# BulkSMS Model
class SentSMSList(models.Model):
    person = models.ForeignKey('PersonList', on_delete=models.CASCADE) 
    phone = models.CharField(max_length=20)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')], default='Success') 
    created = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        db_table = 'sent_sms_list'
        verbose_name = 'Set SMS List' 

    def __str__(self):
        return f"Bulk SMS to {self.person.name} on {self.sent_date}"

 
# BulkEmail Model
class BulkEmail(models.Model):
    person = models.ForeignKey('PersonList', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Sent', 'Sent'), ('Failed', 'Failed')], default='Sent')
    rank = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bulk_email'
        verbose_name = 'Bulk Email'
        verbose_name_plural = 'Bulk Emails'

    def __str__(self):
        return f"Bulk Email to {self.person.name} on {self.sent_date}"


# Organization Model
class Organization(models.Model):
    category = models.ForeignKey('OrganizationCategory', on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)
    # designation = models.ForeignKey('Designation', on_delete=models.CASCADE)
    division = models.ForeignKey('Division', on_delete=models.CASCADE)
    # contact_person_name = models.CharField(max_length=255)
    email1 = models.EmailField(max_length=255, unique=True)
    email2 = models.EmailField(max_length=255, unique=True)
    email3 = models.EmailField(max_length=255, unique=True)
    mobile1 = models.CharField(max_length=30, blank=True, null=True)
    mobile2 = models.CharField(max_length=30, blank=True, null=True)
    mobile3 = models.CharField(max_length=30, blank=True, null=True)
    residential_address = models.TextField(blank=True, null=True)
    office_address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_facebook = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.org_name



# Company Model
class CompanyList(models.Model): 
    category = models.ForeignKey('OrganizationCategory', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    email1 = models.EmailField(max_length=255, unique=True)
    email2 = models.EmailField(max_length=255, unique=True)
    email3 = models.EmailField(max_length=255, unique=True)
    mobile1 = models.CharField(max_length=30, blank=True, null=True)
    mobile2 = models.CharField(max_length=30, blank=True, null=True)
    mobile3 = models.CharField(max_length=30, blank=True, null=True)
    residential_address = models.TextField(blank=True, null=True)
    office_address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_facebook = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True) 
    map_location = models.TextField(blank=True, null=True) 
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'company_list'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name



# OrganizationFollowUp Model
class OrganizationFollowUp(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    follow_up_date = models.DateTimeField()
    status = models.CharField(max_length=255, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization_follow_up'
        verbose_name = 'Organization Follow-Up'
        verbose_name_plural = 'Organization Follow-Ups'

    def __str__(self):
        return f"Follow-up for {self.organization.name} on {self.follow_up_date}"
