import unittest
from application import create_app
from faker import Faker
from unittest.mock import MagicMock, patch



class TestProductionEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app("DevelopmentConfigAssignment")
        app.config['Testing']= True
        
        self.app = app.test_client()

    @patch('services.productionService.Session')
    def test_get(self, mock_production):
        
        faker = Faker()
        product_id, quantity_produced, date_produced = faker.random_digit(), faker.random_digit(), faker.date()
        mock_data = MagicMock()
        mock_data.product_id = product_id
        mock_data.quantity_produced = quantity_produced
        mock_data.date_produced = date_produced
        

        mock_production.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "product_id" : product_id,
            "quantity_produced": quantity_produced,
            "date_produced": date_produced
        }
        self.app.post("/productions/", json=payload)
        response = self.app.get("/productions/", json=payload)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        # self.assertIn("id", response.get_json()[0])
        




    @patch('services.productionService.Session')
    def test_post(self, mock_production):
        # with self.app_context():
        faker = Faker()    
        product_id, quantity_produced, date_produced = faker.random_digit(), faker.random_digit(), faker.date()
        mock_data = MagicMock()
        mock_data.product_id = product_id
        mock_data.quantity_produced = quantity_produced
        mock_data.date_produced = date_produced
        

        mock_production.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "product_id" : product_id,
            "quantity_produced": quantity_produced,
            "date_produced": date_produced
        }
        response = self.app.post("/productions/", json=payload)
        
            
        self.assertEqual(response.status_code, 201)


    @patch('services.productionService.Session')
    def test_fake_post(self, mock_production):
        
            
        faker=Faker()
        product_id, quantity_produced = faker.random_digit(), faker.random_digit()
        mock_data = MagicMock()
        mock_data.product_id = product_id
        mock_data.quantity_produced = quantity_produced
        
        

        mock_production.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "product_id" : product_id,
            "quantity_produced": quantity_produced,
            
        }

        response = self.app.post("/productions/", json=payload)
        
            
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'date_produced': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()
