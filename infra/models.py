from django.db import models

from django.utils.ipv6 import clean_ipv6_address

# Create your models here.

class Retailer(models.Model):
    name = models.CharField(max_length=64)
    contract_id = models.CharField(max_length=32)
    address = models.TextField()
    bank = models.CharField(max_length=128)
    inn = models.CharField(max_length=11)
    ogrn = models.CharField(max_length=13)
    r_acc = models.CharField(max_length=20)
    c_acc = models.CharField(max_length=20)
    bic = models.CharField(max_length=9)
    phone = models.CharField(max_length=12)
    comment = models.TextField(max_length=1024)

    def __unicode__(self):
        return u"{} ({})".format(self.name, self.contract_id)

class Hardware(models.Model):
    serial = models.CharField(max_length=64)
    purchase_date = models.DateField()
    warranty = models.IntegerField(default=0)
    hw_type = models.CharField(max_length=32)
    retailer = models.ForeignKey(Retailer)
    comment = models.TextField()
    location = models.CharField(max_length=128)

    def __unicode__(self):
        return u"{}: {}".format(self.hw_type, self.serial)

class Server(models.Model):
    SERV_TYPE_CHOICES = (('hws', 'hardware server'), 
                         ('kvm', 'KVM guest'))
    hardware = models.ForeignKey(Hardware)
    serv_type = models.CharField(max_length=3, choices=SERV_TYPE_CHOICES)
    config_summary = models.TextField(max_length=255)
    mac = models.CharField(max_length=17)
    kvm_host = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{:=06} ({})".format(self.id, self.mac)

class Build(models.Model):
    prefix = models.CharField(max_length=4, default='fs')
    name = models.CharField(max_length=16, default='generic')
    version = models.CharField(max_length=6)
    revision = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u"{}_{}/{}.{}".format(self.prefix, self.name, self.version, self.revision)

class Node(models.Model):
    hostname = models.CharField(max_length=255)
    server = models.ForeignKey(Server)
    build = models.ForeignKey(Build)
    #FIXME - maybe need separate class for conf_type
    conf_type = models.CharField(max_length=32)

    def __unicode__(self):
        return self.hostname

class Subnet(models.Model):
    IP_PROTOCOL_CHOICES = (('ipv4', 'IPv4 subnet'),
                          ('ipv6', 'IPv6 subnet'))
    net = models.GenericIPAddressField(protocol='both')
    mask = models.PositiveSmallIntegerField()
    protocol = models.CharField(max_length=4, choices=IP_PROTOCOL_CHOICES)
    mark = models.CharField(max_length=8)

    def __unicode__(self):
        return u"{}/{}".format(self.net, self.mask)

class Ip_address(models.Model):
    subnet = models.ForeignKey(Subnet)
    ip = models.GenericIPAddressField(protocol='both')
    node = models.ForeignKey(Node)

    def norm(self):
        if self.subnet.protocol == 'ipv4':
            return clean_ipv6_address(self.ip, True)
        return self.ip

    def __unicode__(self):
        return self.ip

