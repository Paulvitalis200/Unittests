import unittest
from employee import Employee

class TestEmployeee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        self.emp_1 = Employee('Paul', 'Vitalis', 50000)
        self.emp_2 = Employee('Jane', 'Doe', 60000)

    def tearDown(self):
        print('\ntearDown\n')

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Paul.Vitalis@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@email.com')

        self.emp_1.first = 'Kimi'
        self.emp_2.first = 'John'

        
        self.assertEqual(self.emp_1.email, 'Kimi.Vitalis@email.com')
        self.assertEqual(self.emp_2.email, 'John.Doe@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Paul Vitalis')
        self.assertEqual(self.emp_2.fullname, 'Jane Doe')

        self.emp_1.last = 'Otieno'
        self.emp_2.first = 'Cave'

        self.assertEqual(self.emp_1.fullname, 'Paul Otieno')
        self.assertEqual(self.emp_2.fullname, 'Cave Doe')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()