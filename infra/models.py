from django.db import models

# Create your models here.

class Retailer(models.Model):
    name = models.CharField(max_length=64)
    contract_id = models.CharField(max_length=32)
    address = models.TextField()

class Hardware(models.Model):
    serial = models.CharField(max_length=64)
    purchase_date = models.DateField()
    warranty = models.IntegerField(default=0)
    hw_type = models.CharField(max_length=32)
    retailer = models.ForeignKey(Retailer)
    comment = models.TextField()
    location = models.CharField(max_length=128)

class Servers(models.Model):
    SERV_TYPE_CHOICES = (('hws', 'hardware server'), 
                         ('kvm', 'KVM guest'))
    hardware = models.ForeignKey(Hardware)
    serv_type = models.CharField(max_length=3, choices=SERV_TYPE_CHOICES)
    config_summary = models.TextField(max_length=255)
    mac = models.CharField(max_length=17)
    kvm_host = models.BooleanField(default=False)

class Builds(models.Model):
    prefix = models.CharField(max_length=4, default='fs')
    name = models.CharField(max_length=16, default='generic')
    version = models.CharField(max_length=6)
    revision = models.PositiveSmallIntegerField()

class Nodes(models.Model):
    hostname = models.CharField(max_length=255)
    server = models.ForeignKey(Servers)
    build = models.ForeignKey(Builds)
    #FIXME - maybe need separate class for conf_type
    conf_type = models.CharField(max_length=32)

class Subnets(models.Model):
    IP_PROTOCOL_CHOICES = (('ipv4', 'IPv4 subnet'),
                          ('ipv6', 'IPv6 subnet'))
    net = models.GenericIPAddressField(protocol='both')
    mask = models.PositiveSmallIntegerField()
    protocol = models.CharField(max_length=4, choices=IP_PROTOCOL_CHOICES)
    mark = models.CharField(max_length=8)

class Ip_addresses(models.Model):
    subnet = models.ForeignKey(Subnets)
    ip = models.GenericIPAddressField(protocol='both')
    node = models.ForeignKey(Nodes)

