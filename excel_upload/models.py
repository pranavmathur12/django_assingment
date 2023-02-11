from django.db import models
from django.contrib.auth.models import User

# class BaseModel(models.Model):
#     created_at   = models.DateTimeField(auto_now_add=True)
#     updated_at   = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(
#         User,related_name="%(class)s_createdby",
#         on_delete=models.CASCADE,
#         null=True,
#     )
#     updated_by = models.ForeignKey(
#         User,related_name="%(class)s_updatedby",
#         on_delete=models.CASCADE,
#         null=True,
#     )



class Site(models.Model):
    site_id = models.IntegerField(null= True)
    site_name = models.CharField(max_length=100,null=False)
    country = models.CharField(max_length=100,null=False)
    order_id = models.IntegerField(null=False)
    purchase_id = models.IntegerField(null=False)
    csm_name = models.CharField(max_length=100,null=False)
    serial = models.CharField(max_length=100,null=False)
    ip_address = models.CharField(max_length = 100 , null=False)
    model = models.CharField(max_length=100,null=False)
    macaddr = models.CharField(max_length=100 , null=False)



