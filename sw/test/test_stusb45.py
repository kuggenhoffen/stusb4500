import unittest
import mock
import sys
from stusb45 import STUSB4500

class TestSTUSB4500(unittest.TestCase):
    def test_s(self):
        inst = STUSB4500(mock.MagicMock(), 0x12)
        inst.version()


if __name__ == '__main__':
    unittest.main()
