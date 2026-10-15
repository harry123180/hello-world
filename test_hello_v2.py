"""Tests for hello_v2.

Run with the standard library only:
    python -m unittest -v test_hello_v2
"""

import unittest

from hello_v2 import __version__, greet, main


class GreetTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), ["Hello, World!"])

    def test_multiple_names(self):
        self.assertEqual(greet(["Alice", "Bob"]), ["Hello, Alice!", "Hello, Bob!"])

    def test_custom_greeting(self):
        self.assertEqual(greet(["Alice"], greeting="Hi"), ["Hi, Alice!"])

    def test_count_repeats(self):
        self.assertEqual(greet(["A"], count=2), ["Hello, A!", "Hello, A!"])

    def test_shout(self):
        self.assertEqual(greet(["Alice"], shout=True), ["HELLO, ALICE!"])

    def test_blank_names_are_skipped(self):
        self.assertEqual(greet(["", "  ", "Alice"]), ["Hello, Alice!"])

    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            greet(["A"], count=0)


class CliTests(unittest.TestCase):
    def test_version_constant(self):
        self.assertEqual(__version__, "2.0.0")

    def test_main_returns_zero(self):
        self.assertEqual(main(["Alice"]), 0)

    def test_main_rejects_bad_count(self):
        self.assertEqual(main(["Alice", "--count", "0"]), 2)


if __name__ == "__main__":
    unittest.main()
