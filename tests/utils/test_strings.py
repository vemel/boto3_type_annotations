import unittest

from mypy_boto3_builder.utils.strings import (
    get_class_prefix,
    clean_doc,
    wrap_code_line,
    wrap_line,
    get_line_with_indented,
)


class StringsTestCase(unittest.TestCase):
    def test_get_class_prefix(self) -> None:
        self.assertEqual(get_class_prefix("my_func"), "MyFunc")
        self.assertEqual(get_class_prefix(""), "")
        self.assertEqual(get_class_prefix("myFunc"), "MyFunc")

    def test_clean_doc(self) -> None:
        self.assertEqual(clean_doc(None, 80), "")
        self.assertEqual(clean_doc("line trim test   ", 80), "line trim test")
        self.assertEqual(
            clean_doc(r"backslash\\test\here", 80), r"backslash\\test\\here"
        )
        self.assertEqual(
            clean_doc('triple quotes""" test', 80), "triple quotes''' test"
        )
        self.assertEqual(
            clean_doc("trailing lines test \n  \n\n", 80), "trailing lines test"
        )
        self.assertEqual(
            clean_doc("multiple empty lines\n\n\ntest", 80),
            "multiple empty lines\n\ntest",
        )

        self.assertEqual(clean_doc("short line", 11), "short line")
        self.assertEqual(clean_doc("loooooooong line", 11), "loooooooong\nline")
        self.assertEqual(clean_doc("extremely_loong line", 11), "extremely_loong\nline")
        self.assertEqual(clean_doc("many words line", 11), "many words\nline")
        self.assertEqual(
            clean_doc("  preserve indent on split", 11),
            "  preserve\n  indent on\n  split",
        )
        self.assertEqual(
            clean_doc(" line_with=with|many|options", 11),
            " line_with=\n     with\n     |many\n     |options",
        )

    def test_wrap_line(self) -> None:
        self.assertEqual(list(wrap_line("short line", 10)), ["short line"])
        self.assertEqual(
            list(wrap_line("to looooooooooong line", 10)),
            ["to", "looooooooooong", "line"],
        )
        self.assertEqual(
            list(wrap_line("max lenght is 10", 10)), ["max lenght", "is 10"]
        )
        self.assertEqual(
            list(wrap_line("  now with some indent", 10)),
            ["  now with", "  some", "  indent"],
        )
        self.assertEqual(
            list(wrap_line("this_is_a=code|line", 10)),
            ["this_is_a=", "    code", "    |line"],
        )

    def test_wrap_code_line(self) -> None:
        self.assertEqual(list(wrap_code_line("short line", 10)), ["short line"])
        self.assertEqual(
            list(wrap_code_line("to looooooooooong line", 10)),
            ["to looooooooooong line"],
        )
        self.assertEqual(
            list(wrap_code_line("to_looooooooooong_line", 10)),
            ["to_looooooooooong_line"],
        )
        self.assertEqual(
            list(wrap_code_line("this_is_a=code|line", 10)),
            ["this_is_a=", "    code", "    |line"],
        )
        self.assertEqual(
            list(wrap_code_line("test=a|b|c|d", 10)), ["test=", "    a|b|c", "    |d"],
        )
        self.assertEqual(
            list(wrap_code_line("test=a|b|really_long_option|d", 10)),
            ["test=", "    a|b", "    |really_long_option", "    |d"],
        )
        self.assertEqual(
            list(wrap_code_line("my_key=my_looong_value", 10)),
            ["my_key=", "    my_looong_value"],
        )

    def test_get_line_with_indented(self) -> None:
        self.assertEqual(get_line_with_indented("a\n\nb\nc"), "a")
        self.assertEqual(
            get_line_with_indented("a\n\n b\n  c\n\n d\ne"), "a\n\n b\n  c\n\n d"
        )
        self.assertEqual(get_line_with_indented(" a\n  b\n  c\n d"), " a\n  b\n  c")
        self.assertEqual(get_line_with_indented(""), "")
        self.assertEqual(get_line_with_indented("a\n\nb\n c\nd", True), "a\n\nb\n c")
