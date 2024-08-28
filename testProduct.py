import unittest
from application import create_app
from faker import Faker
from unittest.mock import MagicMock, patch



class TestProductEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app("DevelopmentConfigAssignment")
        app.config['Testing']= True
        
        self.app = app.test_client()

    @patch('services.productService.Session')
    def test_get(self, mock_product):
        
        faker = Faker()
        name, price = faker.name(), faker.random_digit()
        mock_data = MagicMock()
        mock_data.name = name
        mock_data.price = price
        

        mock_product.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "name" : name,
            "price": price
        }
        self.app.post("/products/", json=payload)
        response = self.app.get("/products/", json=payload)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        # self.assertIn("id", response.get_json()[0])
        




    @patch('services.productService.Session')
    def test_post(self, mock_product):
        # with self.app_context():
            
        faker=Faker()
        name, price = faker.name(), faker.random_digit()
        mock_data = MagicMock()
        mock_data.name = name
        mock_data.price = price

        mock_product.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "name" : name,
            "price": price
        }

        response = self.app.post("/products/", json=payload)
        
            
        self.assertEqual(response.status_code, 201)


    @patch('services.productService.Session')
    def test_fake_post(self, mock_product):
        
            
        faker=Faker()
        name = faker.name()
        mock_data = MagicMock()
        
        mock_data.name = name
        

        mock_product.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
           
            "name" : name
            
        }

        response = self.app.post("/products/", json=payload)
        
            
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'price': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()



