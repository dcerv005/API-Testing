import unittest
from unittest.mock import MagicMock, patch
from application import create_app
from faker import Faker





class TestOrderEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app("DevelopmentConfigAssignment")
        app.config['Testing']= True
       
        self.app = app.test_client()

    @patch('services.orderService.Session')
    def test_get(self, mock_order):
        
        faker = Faker()
        customer_id, product_id, quantity, total_price = faker.random_digit(), faker.random_digit(), faker.random_digit(), faker.random_digit()
        
        mock_data = MagicMock()
        mock_data.customer_id = customer_id
        mock_data.product_id = product_id
        mock_data.quantity = quantity
        mock_data.total_price = total_price

        mock_order.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "customer_id" : customer_id,
            "product_id" : product_id,
            "quantity": quantity,
            "total_price" : total_price
        }
        self.app.post("/orders/", json=payload)
        response = self.app.get("/orders/", json=payload)
        
        self.assertEqual(response.status_code, 200)
        # self.assertIn("id", response.get_json()[0])
        




    @patch('services.orderService.Session')
    def test_post(self, mock_order):
        
            
        faker = Faker()
        customer_id, product_id, quantity, total_price = faker.random_digit(), faker.random_digit(), faker.random_digit(), faker.random_digit()
        
        mock_data = MagicMock()
        mock_data.customer_id = customer_id
        mock_data.product_id = product_id
        mock_data.quantity = quantity
        mock_data.total_price = total_price

        mock_order.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "customer_id" : customer_id,
            "product_id" : product_id,
            "quantity": quantity,
            "total_price" : total_price
        }

        response = self.app.post("/orders/", json=payload)
       
            
        self.assertEqual(response.status_code, 201)


    @patch('services.orderService.Session')
    def test_fake_post(self, mock_order):
     
            
        faker = Faker()
        customer_id, product_id, quantity= faker.random_digit(), faker.random_digit(), faker.random_digit()
        
        mock_data = MagicMock()
        mock_data.customer_id = customer_id
        mock_data.product_id = product_id
        mock_data.quantity = quantity
       

        mock_order.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "customer_id" : customer_id,
            "product_id" : product_id,
            "quantity": quantity
            
        }

        response = self.app.post("/orders/", json=payload)
        
            
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'total_price': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()