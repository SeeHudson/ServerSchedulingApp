from django.db import models

# Not sure about this one either
class Restaurant(models.Model):
    pass
    # RESTAURANT_ID = models.AutoField(primary_key=True)
    # NAME = models.CharField(max_length=100)
    # ADDRESS = models.CharField(max_length=100)
    # CITY = models.CharField(max_length=100)
    # STATE = models.CharField(max_length=100)
    # ZIP = models.CharField(max_length=100)
    # PHONE = models.CharField(max_length=100)
    # EMAIL = models.CharField(max_length=100)
    # MANAGER_ID = models.ForeignKey('Manager', models.DO_NOTHING, db_column='MANAGER_ID', blank=True, null=True)
    #
    # class Meta:
    #     managed = False
    #     db_table = 'RESTAURANT'
