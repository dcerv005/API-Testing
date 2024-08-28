import unittest
from application import create_app
from faker import Faker
from unittest.mock import MagicMock, patch



class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app("DevelopmentConfigAssignment")
        app.config['Testing']= True
        
        self.app = app.test_client()

    @patch('services.employeeService.Session')
    def test_get(self, mock_employee):
        
        faker = Faker()
        name, position = faker.name(), faker.job()
        mock_data = MagicMock()
        mock_data.name = name
        mock_data.position = position
        

        mock_employee.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "name" : name,
            "position": position
        }
        self.app.post("/employees/", json=payload)
        response = self.app.get("/employees/", json=payload)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        # self.assertIn("id", response.get_json()[0])
        




    @patch('services.employeeService.Session')
    def test_post(self, mock_employee):
        # with self.app_context():
            
        faker=Faker()
        name, position = faker.name(), faker.job()
        mock_data = MagicMock()
        mock_data.name = name
        mock_data.position = position

        mock_employee.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
            "name" : name,
            "position": position
        }

        response = self.app.post("/employees/", json=payload)
        
            
        self.assertEqual(response.status_code, 201)


    @patch('services.employeeService.Session')
    def test_fake_post(self, mock_employee):
        
            
        faker=Faker()
        name = faker.name()
        mock_data = MagicMock()
        
        mock_data.name = name
        

        mock_employee.return_value.scalar_one_or_none.return_value = mock_data
        payload = {
           
            "name" : name
            
        }

        response = self.app.post("/employees/", json=payload)
        
            
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'position': ['Missing data for required field.']})



if __name__ == '__main__':
    unittest.main()
