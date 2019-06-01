from django.contrib import admin
from django.test import TestCase

from .admin import HitterAdmin
from .models import Hitter


class HitterTest(TestCase):
    def test_hitter_model_should_have_email_field(self):
        hitter = Hitter.objects.create(
            email='gatuk@prontomaketing.com'
        )

        self.assertEqual(hitter.email, 'gatuk@prontomaketing.com')


class HitterAdminTest(TestCase):
    def test_hitter_admin_should_be_registered_to_admin(self):
        actualHitterInstance = admin.site._registry[Hitter]
        self.assertIsInstance(actualHitterInstance, HitterAdmin)
