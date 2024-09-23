from django.db import models
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.


class DriverTable(models.Model):
    """
    This contains schema level information
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    short_schema = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # product_id = models.BigAutoField(db_index=True, primary_key=True)
    # name = models.TextField( max_length=255, unique=True,null=True, blank=True)
    # price = models.IntegerField(null=True, blank=True)
    # details = models.CharField( max_length=255, null=True, blank=True)
    # quantity = models.IntegerField(null=True, blank=True)
    # stock = models.IntegerField(null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)


class TableListTable(models.Model):
    """
    This contains table level information
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    short_schema = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class STMTable(models.Model):
    """
    This contains column level details of tables
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    subject_area = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class DataTypes(models.Model):
    """
    This contains list data type supported by ingestion & pipeline process
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    data_type = models.CharField(max_length=255, null=True, blank=True)
    integer_limit = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class File(models.Model):
    """
    This Table Contains details of files
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    file_Name = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    file_type = models.CharField(max_length=20, blank=True)
    file = models.FileField(upload_to="files/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SchemaMetaData(models.Model):
    """
    This class contains schemas meta data that
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    short_schema = models.CharField(max_length=20, blank=True)
    number_of_tables = models.IntegerField(null=True, blank=True)


class HomePageLinks(models.Model):
    """
    This model class will contain information of links & their description
    """
    id = models.BigAutoField(db_index=True, primary_key=True)
    link_name = models.TextField(blank=True)
    link_mapping = models.TextField(blank=True)
    description = models.TextField(blank=True)
    button_style = models.TextField(blank=True, default='btn btn-primary')
    active = models.BooleanField(default=True)


class FileForm(ModelForm):
    """
    This File field form class
    """
    class Meta:
        """
        This class defines form columns
        """
        model = File
        fields = ["file_Name", "description", "file_type", "file"]


class StmMeta(ModelForm):
    """
    This File field form class
    """
    class Meta:
        """
        This class defines form columns
        """
        model = SchemaMetaData
        fields = ["id", "short_schema", "number_of_tables"]
