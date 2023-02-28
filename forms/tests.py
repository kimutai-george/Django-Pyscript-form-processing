from django.test import TestCase
from .models import Details

class DetailsTestCase(TestCase):
    def setUp(self):
        self.model = Details.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@gmail.com'
        )

    def test_model_has_first_name_field(self):
        self.assertTrue('first_name' in [field.name for field in self.model._meta.get_fields()])

    def test_model_has_last_name_field(self):
        self.assertTrue('last_name' in [field.name for field in self.model._meta.get_fields()])

    def test_model_has_email_field(self):
        self.assertTrue('email' in [field.name for field in self.model._meta.get_fields()])

    def test_model_str_method(self):
        expected_str = f'{self.model.first_name} {self.model.last_name}'
        self.assertEqual(str(self.model), expected_str)




