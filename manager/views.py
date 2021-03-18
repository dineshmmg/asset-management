import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from bootstrap.views import login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from import_export.admin import ImportExportModelAdmin
from tablib import Dataset

#here strat the CRUD opration for the assets typs
# list the assets types
@login_required(login_url='/login')
def list_items(request):
    #header = "List of List Items"
    form = assetSearchForm(request.POST or None)
    queryset = asset_types.objects.all()
    context = {
        #"header": header,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = asset_types.objects.filter(table_name__icontains=form['table_name'].value(),
									          asset_tag__icontains=form['asset_tag'].value()
									          )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Asset Types.csv"'
            writer = csv.writer(response)
            writer.writerow(['COUNT', 'TABLE NAME', 'ASSET TAG', 'STATUS'])
            instance = queryset
            for Asset_types in instance:
                writer.writerow([ Asset_types.table_name, Asset_types.asset_tag, Asset_types.status])
            return response

        context = {
        "form": form,
        #"header": header,
        "queryset": queryset,
    }
    return render(request, "list_items.html",context)


        
#add asset types
@login_required(login_url='/login')
def add_items(request):
    form = managercreateform(request.POST or None)
    if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return render(request,'list_items.html')
    context = {
            "form": form,
            "title": "Add Item",
    }
    return render(request, "add_items.html", context)


#update the Asset List Table
@login_required(login_url='/login')
def update_items(request, pk):
    queryset = asset_types.objects.get(id=pk)
    form = assetUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = assetUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Update')
            return redirect('list_items')
    context = {
        'form':form
    }
    return render(request, 'add_items.html', context)

    
#delete the asset types
@login_required(login_url='/login')
def delete_items(request, pk):
    queryset = asset_types.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully delete')
        return redirect('list_items')
    return render(request, 'delete_items.html')

#Here start CRUD operations for the User
#User List Table
@login_required(login_url='/login')
def auth_user(request):
    queryset = User.objects.all()
    context = {
        "queryset": queryset,
    }
    return render(request, "auth_user.html",context)


#add users
@login_required(login_url='/login')
def add_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']   
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('add_user')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('add_user')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'User Created')
                return redirect('auth_user')
                
        else:
            messages.info(request, 'password not matching...')
            return redirect('add_user')
        
           
    else:
        return render(request, "add_user.html")



#Update User List Table
@login_required(login_url='/login')
def update_user(request, pk):
    queryset = User.objects.get(id=pk)
    form = userupdateform(instance=queryset)
    if request.method == 'POST':
        form = userupdateform(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Update')
            return redirect('auth_user')
    context = {
        'form':form
    }
    return render(request, 'update_user.html', context)


#delete users form the user table 
@login_required(login_url='/login')
def delete_user(request, pk):
    queryset = User.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully delete')
        return redirect('auth_user')
    return render(request, 'delete_user.html')


#Here start CRUD opreation for assets
@login_required(login_url='/login')
def table_items(request,asset_type_id_id):
    queryset = asset_types.objects.get(id=asset_type_id_id)
    context = {
        'queryset':queryset
    }
    return render(request, 'table_items.html', context)

#list the assets
@login_required(login_url='/login')
def assets(request):
    form = assetsform(request.POST or None)
    queryset = asset_name.objects.all()
    context = {
        "form": form,
        "queryset":queryset
    }
    if request.method == 'POST':
        queryset = asset_name.objects.filter(name__icontains=form['name'].value(),
                                             asset_tag_number__icontains=form['asset_tag_number'].value())
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Assets.csv"'
            writer = csv.writer(response)
            writer.writerow(['COUNT', 'ASSET TYPE ID', 'ASSET TAG NUMBER', 'NAME','MANUFACTURER',
                             'MODEL','SERIAL NUMBER','CPU','RAM','HDD','OS','SCREEN',
                             'CD DRIVE','DESCRIPTION','MAC ADDRESS','PURCHASE','LOCATION','STATUS'])
            for instance in queryset:
                writer.writerow([instance.id,instance.asset_type_id,instance.asset_tag_number,
                                 instance.name,instance.manufacturer,instance.model,instance.serial_number,
                                 instance.cpu,instance.ram,instance.hdd,instance.os,instance.screen,
                                 instance.cd_drive,instance.description,instance.mac_address,instance.purchase,
                                 instance.location,instance.status])
            return response

        """if form['import_to_CSV'].value() == True:
            new_list = request.FILES['myfile']

            if not new_list.name.endswith('xlsx'):
                messages.info(request,'wrong format')
                return render(request, 'list_items')

            imported_data = dataset.load(new_list.read().format='xlsx')
            for data in imported_data:
                value = asset_name(
                    data[0],data[1],data[2],data[3],
                    data[4],data[5],data[6],data[7],
                    data[8],data[9],data[10],data[11],
                    data[12]data[13],data[14],data[15],
                    data[16],data[17],data[18],
                    )
                value.save()
            return response"""
        
        context = {
        "form": form,
        #"header": header,
        "queryset": queryset,
    }
    return render(request, 'assets.html', context)


#add assets
@login_required(login_url='/login')
def add_assets(request):
    form = assetTableForm(request.POST or None)
    if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('assets')
    context = {
            "form": form,
            "title": "Add Assets",
    }
    return render(request, "add_assets.html", context)



#Update Assets Table
@login_required(login_url='/login')
def update_assets(request, pk):
    queryset = asset_name.objects.get(id=pk)
    form = assetsupdateform(instance=queryset)
    if request.method == 'POST':
        form = assetsupdateform(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Update')
            return redirect('assets')
    context = {
        'form':form
    }
    return render(request, 'add_assets.html', context)


#delete users form the user table 
@login_required(login_url='/login')
def delete_assets(request, pk):
    queryset = asset_name.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully delete')
        return redirect('assets')
    return render(request, 'delete_assets.html')


#Here start CRUD opreation for user assets
@login_required(login_url='/login')
def user_asset(request):
    queryset = user_assets.objects.all()
    context = {
        'queryset':queryset
    }
    return render(request, 'user_assets.html', context)


#add user assets
@login_required(login_url='/login')
def add_user_assets(request):
    form = adduserassets(request.POST or None)
    if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('user_asset')
    context = {
            "form": form,
            "title": "Assign user Assets",
    }
    return render(request, "add_user_assets.html", context)


#unassigned list
@login_required(login_url='/login')
def unassigned_assets(request):
    queryset = asset_name.objects.filter(asset_type_id=None)
    context = {
        'queryset':queryset
    }
    
    return render(request, "unassigned_assets.html",context)



#Update user assets Table
@login_required(login_url='/login')
def update_user_assets(request, pk):
    queryset = user_assets.objects.get(id=pk)
    form = updateuserassets(instance=queryset)
    if request.method == 'POST':
        form = updateuserassets(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Update')
            return redirect('user_asset')
    context = {
        'form':form
    }
    return render(request, 'add_user_assets.html', context)


#delete users form the user assets 
@login_required(login_url='/login')
def delete_user_assets(request, pk):
    queryset = user_assets.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully delete')
        return redirect('user_asset')
    return render(request, 'delete_assets.html')



@login_required(login_url='/login')
def COUNT(request):
    count = asset_name.objects.filter(name='laptop').count()
    print('count')
    context = {
        'count': count
    }
    return render(request, 'list_items.html', context)

        

        



