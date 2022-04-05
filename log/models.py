from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class InputTypes(models.Model):
    type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type


class VehicleTypes(models.Model):
    type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type


class PersonTypes(models.Model):
    type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type


class AttachmentTypes(models.Model):
    type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type


class MasterRecordTypes(models.Model):
    type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type


class EntityRecordTypes(models.Model):
    Entity_type = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.Entity_type


class AdditionalDetails(models.Model):
    display_name = models.CharField(max_length=50)
    type = models.ForeignKey('InputTypes', on_delete=models.CASCADE)
    form = models.ForeignKey('MasterRecordTypes', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.display_name



class MasterRecords(models.Model):
    created     =                models.DateTimeField(auto_now_add=True)
    user        =                models.ForeignKey(User, on_delete=models.PROTECT)
    type        =                models.ForeignKey('MasterRecordTypes', on_delete=models.CASCADE)
    is_active   =                models.BooleanField(default=True)
    violation   =                models.CharField(max_length=50)
    date        =                models.DateField()
    time        =                models.TimeField()
    title       =                models.CharField(max_length=50)
    case_number_regex =          RegexValidator(regex=r'\d{2}-\d{5}',
                                                message='Case Numbers must match the following format: XX-XXXXX ')
    case_number =                models.CharField(validators=[case_number_regex], max_length=8)
    additional_detail = models.JSONField()
    cad_call_number = models.IntegerField()
    cad_id = models.IntegerField()
    rms_case_number = models.IntegerField()
    rms_id = models.IntegerField()


class Vehicles(models.Model):
    created   =                 models.DateTimeField(auto_now_add=True)
    master_record_id = models.ForeignKey('MasterRecords', on_delete=models.CASCADE)
    entity_type      =                 models.ForeignKey('VehicleTypes', on_delete=models.CASCADE)
    make      =                 models.CharField(max_length=50)
    model     =                 models.CharField(max_length=50)
    color     =                 models.CharField(max_length=50)
    state     =                 models.CharField(max_length=50) #make this a dropdown with choices.... we know the states.
    plate     =                 models.CharField(max_length=20)


class Persons(models.Model):
    created            =                 models.DateTimeField(auto_now_add=True)
    master_record_id   =                 models.ForeignKey('MasterRecords', on_delete=models.CASCADE)
    entity_type        =                 models.ForeignKey('PersonTypes', on_delete=models.CASCADE)
    last_name          =                 models.CharField(max_length=50)
    first_name         =                 models.CharField(max_length=50)


class Attachments(models.Model):
    created    =                 models.DateTimeField(auto_now_add=True)
    master_record_id = models.ForeignKey('MasterRecords', on_delete=models.CASCADE)
    entity_type       =                 models.ForeignKey('AttachmentTypes', on_delete=models.CASCADE)
    image      =                 models.FileField()


class Comments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    master_record_id = models.ForeignKey('MasterRecords', on_delete=models.CASCADE)
    comment = models.TextField()


class CustomFields(models.Model):
    type = models.ForeignKey('MasterRecordTypes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
