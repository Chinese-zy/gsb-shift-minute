import unittest
from shifts import assign_minutes
class T(unittest.TestCase):
    def test_total(self):
        r = assign_minutes(0, [1, 2], [{"name": "A", "start": 0, "end": 10}])
        self.assertEqual(len(r), 2)
if __name__ == "__main__":
    unittest.main()
