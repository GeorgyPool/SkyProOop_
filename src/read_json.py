import json
import os


def read_file_json(path_to_js: str) -> list[dict]:
    """Функция принимающая путь до JSON-файла
    и возвращающая список PYTHON
    если файл не найден возвращает пустой список"""

    path_abs = os.path.abspath(path_to_js)
    if os.path.exists(path_abs):
        with open(path_to_js, "r", encoding="utf-8") as file:
            js_list = json.load(file)
        return js_list
    else:
        return []


if __name__ == "__main__":
    print(read_file_json(os.path.join("..", "data", "products.json")))
