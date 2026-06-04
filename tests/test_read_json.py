from unittest.mock import mock_open, patch

from src.read_json import read_file_json


# Проверка read_file_json на позитивный исход
@patch("json.load")
@patch("builtins.open", new_callable=mock_open, read_data="[{'tests': {'hello': 'world'}}]")
@patch("os.path.exists")
def test_read_file_json_is_positive(mock_os, mock_open_func, mock_json_load, return_done_js_list):
    mock_os.return_value = True
    mock_json_load.return_value = return_done_js_list
    result = read_file_json("done.json")
    assert result == return_done_js_list


# Проверка, что read_file_json при отсутствии файла выдает пустой список
@patch("os.path.exists")
def test_read_file_json_not_file(mock_os):
    mock_os.return_value = False
    result = read_file_json("dumps.json")
    assert result == []
