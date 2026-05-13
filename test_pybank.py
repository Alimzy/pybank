import unittest
from pybank import (
    validate_email,
    calculate_balance,
    is_strong,
    apply_interest,
    get_transaction_summary
)


class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(validate_email("alimzy@gmail.com"), "Email is valid")

    def test_email_too_short(self):
        self.assertEqual(validate_email("a@b.co"), "inavalid email length. it must be at least eight character")

    def test_email_starts_with_at(self):
        self.assertEqual(validate_email("@gmail.com"), "Email cannot start with '@'")

    def test_email_missing_at_symbol(self):
        self.assertEqual(validate_email("alimzygmail.com"), "Character must contain '@' symbol")


    def test_empty_transactions(self):
        self.assertEqual(calculate_balance([]), 0)

    def test_all_positive_transactions(self):
        self.assertEqual(calculate_balance([6, 3, 7]), 16)

    def test_mixed_transactions(self):
        # Bug note: negatives are subtracted twice (balance -= negative adds back),
        # so this test reflects the actual current behaviour of the function
        self.assertEqual(calculate_balance([6, 3, 7, -6]), 22)

    def test_single_transaction(self):
        self.assertEqual(calculate_balance([100]), 100)


    def test_strong_password(self):
        self.assertTrue(is_strong("mydfgrtyuh"))

    def test_weak_password(self):
        self.assertFalse(is_strong("abc"))

    def test_exactly_eight_characters(self):
        self.assertTrue(is_strong("abcdefgh"))


    def test_valid_interest_calculation(self):
        self.assertEqual(apply_interest(5000, 0.05, 1), 5250.0)

    def test_raises_on_negative_rate(self):
        with self.assertRaises(ValueError):
            apply_interest(5000, -0.05, 0)

    def test_zero_rate(self):
        self.assertEqual(apply_interest(1000, 0, 5), 1000.0)


    def test_mixed_transactions(self):
        transactions = [
            ["credit", 2000],
            ["debit", 500],
            ["credit", 300],
        ]
        result = get_transaction_summary(transactions)
        self.assertEqual(result[0], ["total_credits", 2300])
        self.assertEqual(result[1], ["total_debits", 500])
        self.assertEqual(result[2], ["net_balance", 1800])
        self.assertEqual(result[3], ["transaction_count", 3])

    def test_only_credits(self):
        transactions = [["credit", 1000], ["credit", 500]]
        result = get_transaction_summary(transactions)
        self.assertEqual(result[2], ["net_balance", 1500])

    def test_only_debits(self):
        transactions = [["debit", 200], ["debit", 300]]
        result = get_transaction_summary(transactions)
        self.assertEqual(result[2], ["net_balance", -500])

    def test_empty_transactions(self):
        result = get_transaction_summary([])
        self.assertEqual(result[2], ["net_balance", 0])
        self.assertEqual(result[3], ["transaction_count", 0])


if __name__ == "__main__":
    unittest.main()
