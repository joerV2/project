
from pathlib import Path


def import_txt(file_path: str | Path) -> str:
    path = Path(file_path)

    if path.suffix.lower() != ".txt":
        raise ValueError("Поддерживаются только файлы TXT")

    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")

    try:
        content = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError("Файл должен иметь кодировку UTF-8") from error

    if not content.strip():
        raise ValueError("Файл пуст")

    return content
