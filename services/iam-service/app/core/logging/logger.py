from loguru import logger
import sys
import os


def configure_logger():
    # Ensure log directory exists
    os.makedirs("logs", exist_ok=True)

    # Remove default logger
    logger.remove()

    # JSON serialization is handled internally by loguru when serialize=True, hence no need for a custom format.
    json_logging_format = {
        "rotation": "10 MB",
        "retention": "10 days",
        "serialize": True,
    }

    # Add file logging for JSON logs
    logger.add("logs/iam_service_info.log", level="INFO", **json_logging_format)
    logger.add("logs/iam_service_error.log", level="ERROR", **json_logging_format)

    # Custom log format for console and stderr
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:" \
                 "<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    # Add console logging
    logger.add(sys.stdout, level="INFO", format=log_format)

    # Add stderr logging
    logger.add(sys.stderr, level="ERROR", backtrace=True, diagnose=True, format=log_format)
