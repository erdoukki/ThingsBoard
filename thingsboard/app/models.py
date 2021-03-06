from django.db import models
from storage import OverwriteStorage


class Connection(models.Model):
    # conection_id = models.AutoField() # already there
    source_address = models.CharField("Source Address", max_length=120)
    destination_address = models.CharField(
        "Destination Address", max_length=120)
    type_of_connection = models.CharField("Connection Type", max_length=120)
    visited = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.source_address + ' - ' + self.destination_address


class URL(models.Model):
    name = models.CharField("Name", max_length=120)
    visited = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Permission(models.Model):
    name = models.CharField("Name", max_length=120)
    urls = models.ManyToManyField(
        URL, related_name='urls_of_perm', null=True, blank=True)
    block = models.BooleanField(default=True)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class State(models.Model):
    name = models.CharField("Name", max_length=120)
    visited = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Room(models.Model):
    """docstring for Room"""
    name = models.CharField("Name", max_length=120)
    permissions = models.ManyToManyField(
        Permission, related_name='perms_of_room', null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Thing_Type(models.Model):
    """docstring for Type"""
    name = models.CharField("Name", max_length=120)
    permissions = models.ManyToManyField(
        Permission, related_name='perms_of_type', null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Owner(models.Model):
    """docstring for Type"""
    name = models.CharField("Name", max_length=120)
    permissions = models.ManyToManyField(
        Permission, related_name='perms_of_owner', null=True, blank=True)
    parent = models.BooleanField(default=False)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Thing(models.Model):

    """Internet of Things"""

    urls_visited = models.ManyToManyField(
        URL, related_name='things_of_url', null=True, blank=True)
    connections = models.ManyToManyField(
        Connection, related_name='things_of_conn', null=True, blank=True)
    states = models.ManyToManyField(
        State, related_name='things_of_state', null=True, blank=True)
    rooms = models.ManyToManyField(
        Room, related_name='things_of_room', null=True, blank=True)
    thing_types = models.ManyToManyField(
        Thing_Type, related_name='things_of_type', null=True, blank=True)
    owners = models.ManyToManyField(
        Owner, related_name='things_of_owner', null=True, blank=True)

    name = models.CharField("Name", max_length=120)
    description = models.CharField("Description", max_length=120, null=True)
    mac_address = models.CharField(
        "MAC Address", max_length=120)
    ip_address = models.CharField("IP address", max_length=120)
    vendor = models.CharField("Vendor", max_length=120)
    admin = models.BooleanField(default=False)
    outside_communication = models.BooleanField(default=True)
    image_file = models.ImageField("Picture", upload_to='image_file',
                                   default='image_file/thing.jpg',
                                   storage=OverwriteStorage(),
                                   blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name
