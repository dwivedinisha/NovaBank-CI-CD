import unittest
from app import health_status, get_account_balance


class TestNovaBank(unittest.TestCase):

    def test_health_status(self):
        result = health_status()
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["app"], "NovaBank")

    def test_account_balance(self):
        result = get_account_balance("ACC101")
        self.assertEqual(result["account_id"], "ACC101")
        self.assertEqual(result["balance"], 2000)


if __name__ == "__main__":
    unittest.main()
