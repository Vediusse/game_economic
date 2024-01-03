import re
from datetime import datetime
from typing import Optional

import jinja2


def unix_to_datetime(unix_timestamp):
    """Преобразование даты в формат datetime."""
    return datetime.fromtimestamp(unix_timestamp)


def render_template(template_name: str, data: Optional[dict] = None) -> str:
    """Конвертирует *.j2 файл в txt"""
    if data is None:
        data = {}
    template = _get_template_env().get_template(template_name)
    rendered = template.render(**data).replace("\n", " ")
    rendered = rendered.replace("<br>", "\n")
    rendered = re.sub(" +", " ", rendered).replace(" .", ".").replace(" ,", ",")
    rendered = "\n".join(line.strip() for line in rendered.split("\n"))
    return rendered


def _get_template_env():
    """Получение директории шаблонов jinja2"""
    if not getattr(_get_template_env, "template_env", None):
        template_loader = jinja2.FileSystemLoader(searchpath="templates")
        env = jinja2.Environment(
            loader=template_loader,
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
        )
        # Добавляем фильтр для шаблона(datetime).
        env.filters["datetime"] = unix_to_datetime

        _get_template_env.template_env = env

    return _get_template_env.template_env
