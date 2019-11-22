import unittest

from mypy_boto3_builder.utils.indent_trimmer import IndentTrimmer


class IndentTrimmerTestCase(unittest.TestCase):
    def test_trim_empty_lines(self) -> None:
        self.assertEqual(
            IndentTrimmer.trim_empty_lines(["", "  asd", " asd", "   asd", "  ", ""]),
            ["  asd", " asd", "   asd"],
        )

    def test_trim_text(self) -> None:
        self.assertEqual(
            IndentTrimmer.trim_text("  asd\n asd\n   asd\n"), " asd\nasd\n  asd\n"
        )

    def test_trim_lines(self) -> None:
        self.assertEqual(
            IndentTrimmer.trim_lines(["  asd", " asd", "   asd"]),
            [" asd", "asd", "  asd"],
        )

    def test_trim_line(self) -> None:
        self.assertEqual(IndentTrimmer.trim_line("     test", 2), "   test")
        self.assertEqual(IndentTrimmer.trim_line("     test", 6), "test")
        self.assertEqual(IndentTrimmer.trim_line("     test", 1), "    test")

    def test_get_line_indent(self) -> None:
        self.assertEqual(IndentTrimmer.get_line_indent("   test"), 3)
        self.assertEqual(IndentTrimmer.get_line_indent("test"), 0)

    def test_indent_line(self) -> None:
        self.assertEqual(IndentTrimmer.indent_line("test", 2), "  test")
        self.assertEqual(IndentTrimmer.indent_line(" test", 2), "   test")
