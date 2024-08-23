import unittest
# import pytest
from unittest.mock import MagicMock, patch
# from application import app
from database import db
from faker import Faker
from services.customerService import save




class TestCustomerEndpoints(unittest.TestCase):

    @patch('services.customerService.session.begin()')
    def test_post(self, mock_customer):
        # with app.app_context():
            
        faker=Faker()
        mock_data = MagicMock()
        mock_data.name = faker.name
        mock_data.email = faker.email
        mock_data.phone = faker.phone_number

        mock_customer.return_value.scalar_one_or_none.return_value = mock_data

        response = save(mock_data)

        # self.assertEqual(response['name'], mock_data.naSme)
            
        self.assertIsNone(response)



if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     pytest.main([__file__])