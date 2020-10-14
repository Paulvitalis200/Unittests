import unittest
from employee import Employee

class TestEmployeee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Paul', 'Vitalis', 50000)
        emp_2 = Employee('Jane', 'Doe', 40000)

        self.assertEqual(emp_1.email, 'Paul.Vitalis@email.com')
        self.assertEqual(emp_2.email, 'Jane.Doe@email.com')

        emp_1.first = 'Kimi'
        emp_2.first = 'John'

        
        self.assertEqual(emp_1.email, 'Kimi.Vitalis@email.com')
        self.assertEqual(emp_2.email, 'John.Doe@email.com')

    def test_fullname(self):
        emp_1 = Employee('Paul', 'Vitalis', 50000)
        emp_2 = Employee('Jane', 'Doe', 40000)

        self.assertEqual(emp_1.fullname, 'Paul Vitalis')
        self.assertEqual(emp_2.fullname, 'Jane Doe')

        emp_1.last = 'Otieno'
        emp_2.first = 'Cave'

        self.assertEqual(emp_1.fullname, 'Paul Otieno')
        self.assertEqual(emp_2.fullname, 'Cave Doe')

    def test_apply_raise(self):
        emp_1 = Employee('Paul', 'Vitalis', 50000)
        emp_2 = Employee('Jane', 'Doe', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()