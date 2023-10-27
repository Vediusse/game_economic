import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    """Базовая настройка логирования"""
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    # Настраиваем логирование в файл
    log_file_handler = RotatingFileHandler(
        "logs/log.txt", maxBytes=10 * 1024 * 1024, backupCount=6
    )
    log_file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    log_file_handler.setFormatter(log_file_format)
    log_file_handler.setLevel(logging.WARNING)

    # Настраиваем вывод в консоль
    console_handler = logging.StreamHandler()
    console_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_format)
    console_handler.setLevel(logging.INFO)

    # Получаем корневой логгер и добавляем обработчики
    logger = logging.getLogger()
    logger.addHandler(log_file_handler)
    logger.addHandler(console_handler)
