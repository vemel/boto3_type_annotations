import unittest
from unittest.mock import patch

from mypy_boto3_builder.utils.strings import get_class_prefix, clean_doc


class StringsTestCase(unittest.TestCase):
    def test_get_class_prefix(self) -> None:
        self.assertEqual(get_class_prefix("my_func"), "MyFunc")
        self.assertEqual(get_class_prefix(""), "")
        self.assertEqual(get_class_prefix("myFunc"), "MyFunc")

    def test_clean_doc(self) -> None:
        self.assertEqual(clean_doc(None), "")
        self.assertEqual(clean_doc("line trim test   "), "line trim test")
        self.assertEqual(clean_doc(r"backslash\\test\here"), r"backslash\\test\\here")
        self.assertEqual(clean_doc('triple quotes""" test'), "triple quotes''' test")
        self.assertEqual(
            clean_doc("trailing lines test \n  \n\n"), "trailing lines test\n"
        )
        self.assertEqual(
            clean_doc("multiple empty lines\n\n\ntest"), "multiple empty lines\n\ntest"
        )

        with patch("mypy_boto3_builder.utils.strings.LINE_LENGTH", 11):
            self.assertEqual(clean_doc("short line"), "short line")
            self.assertEqual(clean_doc("loooooooong line"), "loooooooong\nline")
            self.assertEqual(clean_doc("extremely_loong line"), "extremely_loong\nline")
            self.assertEqual(clean_doc("many words line"), "many words\nline")
            self.assertEqual(
                clean_doc("  preserve indent on split"),
                "  preserve\n  indent on\n  split",
            )
            print(clean_doc(repr(" line_with=with|many|options")))
            self.assertEqual(
                clean_doc(" line_with=with|many|options"),
                " line_with=\n     with\n     |many\n     |options",
            )
