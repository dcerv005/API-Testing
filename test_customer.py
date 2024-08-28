import unittest
# import pytest
from unittest.mock import MagicMock, patch
from application import create_app

from faker import Faker





class TestCustomerEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app("DevelopmentConfigAssignment")
        app.config['Testing']= True
        # blue_print_config(app)
        self.app = app.test_client()

    @patch('services.customerService.Session')
    def test_get(self, mock_customer):
        
        faker = Faker()
        name, email, phone = faker.name(), faker.email(), faker.phone_number()
        mock_data = MagicMock()
        mock_data.name = name
        mock_data.email = email
        mock_data.phone = phone

        mock_customer.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "name" : name,
            "email" : email,
            "phone": phone
        }
        self.app.post("/customers/", json=payload)
        response = self.app.get("/customers/", json=payload)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.get_json()[0])
        




    @patch('services.customerService.Session')
    def test_post(self, mock_customer):
        # with self.app_context():
            
        faker=Faker()
        name, email, phone = faker.name(), faker.email(), faker.phone_number()
        mock_data = MagicMock()
        mock_data.name = name
        mock_data.email = email
        mock_data.phone = phone

        mock_customer.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "name" : name,
            "email" : email,
            "phone": phone
        }

        response = self.app.post("/customers/", json=payload)
        # breakpoint()
        # self.assertEqual(response['name'], mock_data.naSme)
            
        self.assertEqual(response.status_code, 201)


    @patch('services.customerService.Session')
    def test_fake_post(self, mock_customer):
         # with self.app_context():
            
        faker=Faker()
        email, phone = faker.email(), faker.phone_number()
        mock_data = MagicMock()
        
        mock_data.email = email
        mock_data.phone = phone

        mock_customer.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
           
            "email" : email,
            "phone": phone
        }

        response = self.app.post("/customers/", json=payload)
        # breakpoint()
        # self.assertEqual(response['name'], mock_data.naSme)
            
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'name': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     pytest.main([__file__])