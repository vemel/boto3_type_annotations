import unittest
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.logger import get_logger


class LoggerTestCase(unittest.TestCase):
    @patch("mypy_boto3_builder.logger.logger")
    @patch("mypy_boto3_builder.logger.logging")
    def test_get_logger(self, logging_mock: MagicMock, logger_mock: MagicMock) -> None:
        logger_mock.handlers = []
        result = get_logger(verbose=True)
        self.assertEqual(result, logger_mock)
        logging_mock.StreamHandler.assert_called_with()
        logger_mock.set_level.assert_called_with(logging_mock.DEBUG)

        logging_mock.reset_mock()
        HandlerMock = MagicMock()
        logger_mock.handlers = [HandlerMock]
        result = get_logger()
        logging_mock.StreamHandler.assert_not_called()
        logger_mock.setLevel.assert_not_called()
