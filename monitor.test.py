import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertFalse(vitals_ok(99, 102, 70))
        self.assertTrue(vitals_ok(98.1, 70, 98))
        self.assertFalse(vitals_ok(98.1, 70, 98, bp=(150, 95)))
        self.assertFalse(vitals_ok(98.1, 70, 98, respiration=25))
        self.assertFalse(vitals_ok(98.1, 70, 98, bp=(150, 95), respiration=25))
        self.assertTrue(vitals_ok(98.1, 70, 98, bp=(120, 80), respiration=15))

if __name__ == '__main__':
  unittest.main()
