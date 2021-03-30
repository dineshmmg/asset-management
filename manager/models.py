from django.db import models
from django.contrib.auth.models import User, auth

class asset_types(models.Model):
    table_name = models.CharField(blank=True, max_length=45)
    asset_tag = models.CharField(blank=True, max_length=45)
    status = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.table_name


    @property
    def asset_count(self):
        count = self.display.all().count()
        return count
    
    
    
class asset_name(models.Model):
    name = models.CharField(blank=True,null=True,max_length=45)
    asset_tag_number = models.CharField(blank=True,null=True,max_length=45)
    manufacturer = models.CharField(blank=True,null=True,max_length=45)
    model = models.CharField(blank=True,null=True,max_length=45)
    cpu = models.CharField(blank=True,null=True,max_length=45)
    ram = models.CharField(blank=True,null=True,max_length=45)
    hdd = models.CharField(blank=True,null=True,max_length=45)
    os = models.CharField(blank=True,null=True,max_length=45)
    screen = models.CharField(blank=True,null=True,max_length=45)
    cd_drive = models.CharField(blank=True,null=True,max_length=45)
    description = models.CharField(blank=True,null=True,max_length=45)
    serial_number = models.CharField(blank=True,null=True,max_length=45)
    mac_address = models.CharField(blank=True,null=True,max_length=45)
    purchase = models.DateField()
    location = models.CharField(blank=True,null=True,max_length=45)
    status = models.IntegerField(blank=True,null=True)
    asset_type_id = models.ForeignKey(asset_types, on_delete=models.CASCADE,related_name="display")
    
    def __str__(self):
        return self.asset_tag_number
    
    


class user_assets(models.Model):
    asset_type_id = models.ForeignKey(asset_types, blank=True, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    asset_id = models.IntegerField(blank=True,null=True)
    assigned_date = models.DateField()
    return_date = models.DateField()
    serial_number = models.CharField(blank=True,null=True,max_length=45)
    description = models.CharField(blank=True,null=True,max_length=45)
    status = models.IntegerField()
    
    def __str__(self):
        return str(self.user_id)

    
   
    