from django.contrib import admin
from django.test import TestCase

from ..admin import HitterAdmin
from ..models import Hitter


class HitterAdminTest(TestCase):
    def test_hitter_admin_should_be_registered_to_admin(self):
        actualHitterInstance = admin.site._registry[Hitter]
        self.assertIsInstance(actualHitterInstance, HitterAdmin)

    def test_hitter_admin_should_display_email(self):
        expected = ('email',)

        self.assertEqual(HitterAdmin.list_display, expected)
