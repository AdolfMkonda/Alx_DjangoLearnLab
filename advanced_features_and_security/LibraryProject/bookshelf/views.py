from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required



# Create your views here.

group, created = Group.objects.get_or_create(name='Editors')
if created:
    print("Group 'Editors' created.")
else:
    print("Group 'Editors' already exists.")

can_edit_permission = Permission.objects.get(codename='can_edit')
group.permissions.add(can_edit_permission)
print("Permission 'can_edit' added to group 'Editors'.")

group, created = Group.objects.get_or_create(name='Viewers')
if created:
    print("Group 'Viewers' created.")
else:
    print("Group 'Viewers' already exists.")
can_view_permission = Permission.objects.get(codename='can_view')
group.permissions.add(can_view_permission)
print("Permission 'can_view' added to group 'Viewers'.")


group, created = Group.objects.get_or_create(name='Admins')
if created:
    print("Group 'Admins' created.")
else:
    print("Group 'Admins' already exists.")
can_delete_permission = Permission.objects.get(codename='can_delete')
group.permissions.add(can_delete_permission)
print("Permission 'can_delete' added to group 'Admins'.")
can_edit_permission = Permission.objects.get(codename='can_edit')

group.permissions.add(can_edit_permission)
print("Permission 'can_edit' added to group 'Admins'.")
can_view_permission = Permission.objects.get(codename='can_view')
group.permissions.add(can_view_permission)
print("Permission 'can_view' added to group 'Admins'.")

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    return render(request, 'bookshelf/view_books.html') 

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_books(request):
    return render(request, 'bookshelf/edit_books.html') 

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_books(request):
    return render(request, 'bookshelf/delete_books.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_books(request):
    return render(request, 'bookshelf/create_books.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return render(request, 'bookshelf/book_list.html')


    