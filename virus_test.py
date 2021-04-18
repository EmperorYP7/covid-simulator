import unittest
import virus


class TestVirus(unittest.TestCase):
    def test_init(self):
        CUSTOM_PARAMS = {
            "r0": -1,
            "incubation": 5,
            "percent_mild": 0.8,
            "mild_recovery": (7, 14),
            "percent_severe": 0.2,
            "severe_recovery": (21, 42),
            "severe_death": (14, 56),
            "fatality_rate": 0.034,
            "serial_interval": 7,
            "population": 10
        }
        self.assertRaises(ValueError, virus.Virus, CUSTOM_PARAMS)


if __name__ == '__main__':
    unittest.main()
