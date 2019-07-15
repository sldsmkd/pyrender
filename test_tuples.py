import unittest

from pyrender import Tuple, Vector, Point

class TestTuples(unittest.TestCase):
    def tuple_with_w1_isa_point(self):
        tuple = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(tuple.x, 4.2)
        self.assertEqual(tuple.y, -4.2)
        self.assertEqual(tuple.w, 3.1)
        self.assertEqual(tuple.w, 1.0)
        self.assertTrue(tuple.IsPoint())
        self.assertFalse(tuple.IsVector())

# Scenario: A tuple with w=1.0 is a point
#   Given a ← tuple(4.3, -4.2, 3.1, 1.0)
#   Then a.x = 4.3
#     And a.y = -4.2
#     And a.z = 3.1
#     And a.w = 1.0
#     And a is a point
#     And a is not a vector

# Scenario: A tuple with w=0 is a vector
#   Given a ← tuple(4.3, -4.2, 3.1, 0.0)
#   Then a.x = 4.3
#     And a.y = -4.2
#     And a.z = 3.1
#     And a.w = 0.0
#     And a is not a point
#     And a is a vector

if __name__ == '__main__':
    unittest.main()
