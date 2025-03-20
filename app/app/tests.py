from django.test import SimpleTestCase


from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(1 , 0)
        self.assertEqual(res , 1)

    def test_multiply(self):
        res = calc.multiply(2,2)
        self.assertEqual(res , 4)