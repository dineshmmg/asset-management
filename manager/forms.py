from django import forms
from .models import *
from django.contrib.auth.models import User, auth
from import_export.admin import ImportExportModelAdmin

    
class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password']

    
class userupdateform(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username','email','is_superuser','is_staff']
    
    


class managercreateform(forms.ModelForm):
    class Meta:
        model = asset_types
        fields = ['table_name','asset_tag','status']
        
        
    def clean_table_name(self):
        table_name = self.cleaned_data.get('table_name')
        if not table_name:
            raise forms.ValidationError('This field is required')
        for instance in asset_types.objects.all():
            if instance.table_name == table_name:
                raise forms.ValidationError(table_name + ' is already created')
        return table_name
    
    def clean_asset_tag(self):
        asset_tag = self.cleaned_data.get('asset_tag')
        if not asset_tag:
            raise forms.ValidationError('This field is required')
        return asset_tag

        
class assetSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   class Meta:  
     model = asset_types
     fields = ['table_name', 'asset_tag']
     
     
     
class assetUpdateForm(forms.ModelForm):
	class Meta:
		model = asset_types
		fields = ['table_name', 'asset_tag', 'status']
  
  
class assetTableForm(forms.ModelForm):
	class Meta:
		model = asset_name
		fields = "__all__"
    
class assetsupdateform(forms.ModelForm):
    class Meta:
        model = asset_name
        fields ="__all__"
        
        
        
class userassets(forms.ModelForm):
    class Meta:
        model = user_assets
        fields ="__all__"
        
        
class adduserassets(forms.ModelForm):
	class Meta:
		model = user_assets
		fields = "__all__"


class updateuserassets(forms.ModelForm):
    class Meta:
        model = user_assets
        fields ="__all__"
        

#form for the export and search for assets
class assetsform(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   import_to_CSV = forms.BooleanField(required=False)
   class Meta:  
     model = asset_name
     fields = ['name','asset_tag_number'] 
        
    
#class ViewAdmin(ImportExportModelAdmin):
 #   pass