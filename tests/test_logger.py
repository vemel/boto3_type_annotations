import unittest
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.logger import get_logger


class IndentTrimmerTestCase(unittest.TestCase):
    @patch("mypy_boto3_builder.logger.logging")
    def test_get_logger(self, logging_mock: MagicMock) -> None:
        logging_mock.getLogger().handlers = []
        result = get_logger(verbose=True)
        logging_mock.getLogger.assert_called_with("mypy_boto3_builder")
        self.assertEqual(result, logging_mock.getLogger())
        logging_mock.StreamHandler.assert_called_with()
        logging_mock.getLogger().setLevel.assert_called_with(logging_mock.DEBUG)

        logging_mock.reset_mock()
        HandlerMock = MagicMock()
        logging_mock.getLogger().handlers = [HandlerMock]
        result = get_logger()
        logging_mock.StreamHandler.assert_not_called()
        logging_mock.getLogger().setLevel.assert_not_called()
