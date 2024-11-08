import unittest
from src.services.brute_force_service import estimate_crack_time

class TestBruteForceService(unittest.TestCase):
    def test_simple_password_amateur(self):
        result = estimate_crack_time("password", "amateur")
        self.assertIn("Estimated time to crack password", result)

    def test_complex_password_organization(self):
        result = estimate_crack_time("Pa$$w0rd!", "organization")
        self.assertIn("Estimated time to crack password", result)

if __name__ == "__main__":
    unittest.main()