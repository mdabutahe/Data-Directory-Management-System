from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from directory_app.models import *
# Create your views here.
def organizationAdd(request):

    return render(request, 'admin/organizations.html')
 
def division_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        rank = request.POST.get('rank', 1)

        Division.objects.create(name=name, description=description, rank=rank)
        messages.success(request, "Division added successfully!")
        return redirect('division_list')

    return render(request, 'settings/division_add.html')

def division_list(request):
    division_list = Division.objects.all().order_by('rank')
    return render(request, 'settings/division_list.html', {'division_list': division_list})

def division_edit(request, id):
    division  = get_object_or_404(Division, id=id)

    if request.method == 'POST':
        division.name = request.POST.get('name')
        division.description = request.POST.get('description', '')
        division.rank = request.POST.get('rank', 1)
        division.save()

        messages.success(request, "Division updated successfully!")
        return redirect('division_list')

    return render(request, 'settings/division_add.html', {'division': division})

def division_delete(request, id):
    division = get_object_or_404(Division, id=id)
    division.delete()
    messages.success(request, "Division deleted successfully!")
    return redirect('division_list')






################ Organization Category Start here ############### 

def organization_category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        rank = request.POST.get('rank', 1)

        OrganizationCategory.objects.create(name=name, description=description, rank=rank)
        messages.success(request, "Organization category added successfully!")
        return redirect('organization_category_list')

    return render(request, 'settings/organization_category_add.html')

def organization_category_list(request):
    categories = OrganizationCategory.objects.all().order_by('rank')
    return render(request, 'settings/organization_category_list.html', {'categories': categories})

def organization_category_edit(request, id):
    category = get_object_or_404(OrganizationCategory, id=id)

    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description', '')
        category.rank = request.POST.get('rank', 1)
        category.save()

        messages.success(request, "Organization category updated successfully!")
        return redirect('organization_category_list')

    return render(request, 'settings/organization_category_add.html', {'category': category})

def organization_category_delete(request, id):
    category = get_object_or_404(OrganizationCategory, id=id)
    category.delete()
    messages.success(request, "Organization category deleted successfully!")
    return redirect('organization_category_list')



################## Designation Views #########################
def designation_list(request):
    designations = Designation.objects.all()
    return render(request, 'settings/designation_list.html', {'designations': designations})

def designation_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Designation.objects.create(name=name)
        messages.success(request, "Designation added successfully!")
        return redirect('designation_list')

    return render(request, 'settings/designation_add.html')

def designation_edit(request, pk):
    designation = get_object_or_404(Designation, pk=pk)

    if request.method == "POST":
        designation.name = request.POST.get('name')
        designation.save()
        messages.success(request, "Designation updated successfully!")
        return redirect('designation_list')

    return render(request, 'settings/designation_edit.html', {'designation': designation})

def designation_delete(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    designation.delete()
    messages.success(request, "Designation deleted successfully!")
    return redirect('designation_list')




################## Person Level Views #########################
def personlevel_list(request):
    person_levels = PersonLevel.objects.all()
    return render(request, 'settings/personlevel_list.html', {'person_levels': person_levels})

def personlevel_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        PersonLevel.objects.create(name=name)
        messages.success(request, "Person Level added successfully!")
        return redirect('personlevel_list')

    return render(request, 'settings/personlevel_add.html')

def personlevel_edit(request, pk):
    person_level = get_object_or_404(PersonLevel, pk=pk)

    if request.method == "POST":
        person_level.name = request.POST.get('name')
        person_level.save()
        messages.success(request, "Person Level updated successfully!")
        return redirect('personlevel_list')

    return render(request, 'settings/personlevel_edit.html', {'person_level': person_level})

def personlevel_delete(request, pk):
    person_level = get_object_or_404(PersonLevel, pk=pk)
    person_level.delete()
    messages.success(request, "Person Level deleted successfully!")
    return redirect('personlevel_list')










