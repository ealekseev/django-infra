from django.test import TestCase
from django_project.infra.models import *

# Create your tests here.

class InfraTestCase(TestCase):
    def setUp(self):
        Retailer.objects.create(name="ooo RiK",
                                contract_id="00001",
                                address="Address",
                                bank="Sberbank",
                                inn="00000000001",
                                ogrn="0000000000001",
                                r_acc="00000000000000000001",
                                c_acc="00000000000000000001",
                                bic="000000001",
                                phone="89211234567",
                                comment="foobar")
        Hardware.objects.create(serial="00001",
                                purchase_date="2014-05-15",
                                warranty=36,
                                hw_type="server",
                                retailer=Retailer.objects.all()[0],
                                comment="foobar",
                                location="datacenter")
        Server.objects.create(hardware=Hardware.objects.all()[0],
                              serv_type='hws',
                              config_summary="foobar",
                              mac="00:00:00:00:00:aa",
                              kvm_host=False)
        Build.objects.create(prefix="aa",
                             name="build",
                             version="201405",
                             revision="0")

    def test_retailers(self):
        """Retailer display correct id string."""
        retailer = Retailer.objects.get(contract_id="00001")
        self.assertIsInstance(retailer, Retailer)
        self.assertEqual(unicode(retailer), u"ooo RiK (00001)")

    def test_hardware(self):
        hardware = Hardware.objects.get(serial="00001")
        self.assertIsInstance(hardware, Hardware)
        self.assertEqual(unicode(hardware), u"server: 00001")
        self.assertIsInstance(hardware.retailer, Retailer)

    def test_server(self):
        server = Server.objects.get(mac="00:00:00:00:00:aa")
        self.assertIsInstance(server.hardware, Hardware)
        self.assertEqual(server.config_summary, "foobar")

    def test_build(self):
        build = Build.objects.all()[0]
        self.assertEqual(unicode(build), u"aa_build/201405.0")
