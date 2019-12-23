import unittest
from unittest.mock import patch, MagicMock

from black import NothingChanged

from mypy_boto3_builder.writers.utils import blackify, render_jinja2_template


class UtilsTestCase(unittest.TestCase):
    @patch("mypy_boto3_builder.writers.utils.black")
    def test_blackify(self, black_mock: MagicMock) -> None:
        file_path_mock = MagicMock()
        file_path_mock.suffix = ".txt"
        result = blackify("my content", file_path_mock)
        self.assertEqual(result, "my content")

        file_path_mock.suffix = ".py"
        result = blackify("my content", file_path_mock)
        self.assertEqual(result, black_mock.format_file_contents())
        black_mock.FileMode.assert_called_with(is_pyi=False, line_length=100)

        file_path_mock.suffix = ".pyi"
        result = blackify("my content", file_path_mock)
        self.assertEqual(result, black_mock.format_file_contents())
        black_mock.FileMode.assert_called_with(is_pyi=True, line_length=100)

        black_mock.format_file_contents.side_effect = IndentationError()
        with self.assertRaises(ValueError):
            blackify("my content", file_path_mock)

        black_mock.format_file_contents.side_effect = NothingChanged()
        self.assertEqual(blackify("my content", file_path_mock), "my content")

    @patch("mypy_boto3_builder.writers.utils.TEMPLATES_PATH")
    @patch("mypy_boto3_builder.writers.utils.JinjaManager")
    def test_render_jinja2_template(
        self, JinjaManagerMock: MagicMock, TEMPLATES_PATH_MOCK: MagicMock
    ) -> None:
        template_path_mock = MagicMock()
        result = render_jinja2_template(template_path_mock, "package", "service_name")
        JinjaManagerMock.get_environment.assert_called_with()
        JinjaManagerMock.get_environment().get_template.assert_called_with(
            template_path_mock.as_posix()
        )
        JinjaManagerMock.get_environment().get_template().render.assert_called_with(
            package="package", service_name="service_name"
        )
        self.assertEqual(
            result, JinjaManagerMock.get_environment().get_template().render(),
        )

        TEMPLATES_PATH_MOCK.__truediv__().exists.return_value = False
        with self.assertRaises(ValueError):
            render_jinja2_template(template_path_mock, "package", "service_name")
