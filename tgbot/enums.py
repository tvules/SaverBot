from enum import Enum


class MIMEType(str, Enum):
    """List of Internet Media Types."""

    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


class Answer(str, Enum):
    GREETING = "👋🏻 Привет, {}!"
    HELP = (
        "Отправь мне файл excel с полями: title, url, xpath. "
        "Я добавлю эту информацию в базу данных."
    )
    ERROR = "🚨 Не удалось обработать данные.\n" "Ошибка: {}."
    SUCCESS = "Данные успешно добавлены:\n" "{}"


class ProcessErrorDesc(str, Enum):
    INTEGRITYERROR = "В таблице отсутствуют необходимые данные"
    OPERATIONALERROR = "В таблице присутствуют лишние поля"
