import unittest, my_math

class ProductTestCase(unittest.TestCase):
 def test_integer_product(self):
  for x in range(-10,10):
   for y in range(-10,10):
    p = my_math.product(x,y)
    self.assertEqual(p,x*y,'Integer multiplication failed')
 
 def test_float_product(self):
  for x in range(-10,10):
   for y in range(-10,10):
    p = my_math.product(x,y)
    self.assertEqual(p,x*y,'Float multiplication failed')

 def test_integer_product1(self):
  for x in range(-10,10):
   for y in range(-10,10):
    p = my_math.product1(x,y)
    self.assertEqual(p,x*y,'Integer multiplication failed')


if __name__ == "__main__":
 unittest.main()
