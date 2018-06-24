import unittest
from flask_api import app
 
class TestBasicFunction(unittest.TestCase):
    def __init__():
        pass
    def setUp(self):
    	app.testing = True
    	app.config['TESTING'] = True
    	self.app = app.client.post()
        return app

    #def test(self):
    #    self.assertTrue(True)
    def test_4(self):
        #self.func.increment_state()
        result=self.app.get('/fib/10',hostname='localhost',port='8000')
        #result=self.app.client.get('/fib/10')
        print(result)
        #self.assertEqual(app.run('-1'), 'Seems to be you enterd unsupported value\n')
 
if __name__ == '__main__':
    unittest.main()
