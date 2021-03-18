from django.contrib import admin
from .models import *
from .forms import *
from import_export.admin import ImportExportModelAdmin

class managercreateadmin(admin.ModelAdmin):
    list_display = ['table_name','status']
    form = managercreateform
    list_filter = ['table_name']
    search_fields = ['table_name']
    
    
class assetTableForm(admin.ModelAdmin):
    list_display = ['asset_type_id', 'name']
    form = assetTableForm
    
    
class userassets(admin.ModelAdmin):
    list_display = ['user_id', 'asset_type_id']
    form = userassets
    
#@admin.register(asset_name)
class ViewAdmin(ImportExportModelAdmin):
    pass

    
# Register your models here.
admin.site.register(asset_types, managercreateadmin)
admin.site.register(asset_name, ViewAdmin)
admin.site.register(user_assets, userassets)