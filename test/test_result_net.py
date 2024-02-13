import unittest
from main.result_net import file_processing


class TestIPFound(unittest.TestCase):

    def test_from_doc(self):
        self.assertEqual(file_processing("ipv4.txt", "4"), "Result net: 192.168.0.0/23")

    def test_new_data(self):
        self.assertEqual(file_processing("ipv4_1.txt", "4"), "Result net: 192.168.0.0/25")
        self.assertEqual(file_processing("ipv4_2.txt", "4"), "Result net: 192.168.0.0/23")
        self.assertEqual(file_processing("ipv4_6.txt", "4"), "Result net: 0.0.0.0/1")
        self.assertEqual(file_processing("ipv4_8.txt", "4"), "Result net: 192.168.1.0/27")

    def test_error(self):
        self.assertRaises(ValueError, file_processing, "ipv4_3.txt", "4")
        self.assertRaises(ValueError, file_processing, "ipv4_4.txt", "4")
        self.assertRaises(ValueError, file_processing, "ipv4_5.txt", "4")
        self.assertRaises(ValueError, file_processing, "ipv4_7.txt", "4")
